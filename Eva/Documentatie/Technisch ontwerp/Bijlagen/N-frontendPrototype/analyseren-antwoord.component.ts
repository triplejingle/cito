import {HttpErrorResponse, HttpEventType} from '@angular/common/http';

import {Component, ElementRef, OnInit, ViewChild} from '@angular/core';
import {of} from 'rxjs';
import {catchError, map} from 'rxjs/operators';
import {ApiService} from '../api.service';
import {Level} from '../objects/level';
import {PropertyExtractionScript} from '../objects/propertyExtractionScript';


@Component({
  selector: 'app-analyseren-antwoord',
  templateUrl: './analyseren-antwoord.component.html',
  styleUrls: ['./analyseren-antwoord.component.scss']
})

export class AnalyserenAntwoordComponent implements OnInit {

  constructor(private service: ApiService) {
  }

  @ViewChild('fileUpload', {static: false}) fileUpload: ElementRef;
  files = [];

  levels: Level[] = [];

  filter: Level[] = new Array();
  properties: PropertyExtractionScript[] = [];
  desiredProperties = [];

  columns = [];
  rows = [];

  filteredLevels = [];

  ngOnInit() {
    this.getProperties();
  }

  getProperties() {
    this.service.getProperties().subscribe((properties: string[]) => {
      this.properties = [];
      this.properties.pop();
      for (let i = 0; i < properties.length; i++) {
        const script: PropertyExtractionScript = {PropertyExtractionScript: properties[i]};
        this.properties.push(script);
        console.log(properties[i]);
      }
      console.log(this.properties);
    });
  }

  uploadFile(file) {
    const formData = new FormData();
    formData.append('file', file.data);
    file.inProgress = true;
    this.service.upload(formData).pipe(
      map(event => {
        switch (event.type) {
          case HttpEventType.UploadProgress:
            break;
          case HttpEventType.Response:
            return event;
        }
      }),
      catchError((error: HttpErrorResponse) => {
        file.inProgress = false;
        return of(`${file.data.name} upload failed.`);
      })).subscribe((event: any) => {
      if (typeof (event) === 'object') {
        console.log(event.body);
      }
      this.setCriteria();
    });

  }

  private uploadFiles() {
    this.fileUpload.nativeElement.value = '';
    this.files.forEach(file => {
      this.uploadFile(file);
      console.log(file);
    });
  }

  private setCriteria() {
    this.service.getCriteria().subscribe((data: string[]) => {
      const keys = Object.keys(data);
      for (let i = 0; i < keys.length; i++) {
        const variables: string[] = data[keys[i]];
        const niveau: Level = {name: keys[i], variables};
        this.levels[i] = (niveau);
      }
    });
  }

  onClick() {
    const fileUpload = this.fileUpload.nativeElement;
    fileUpload.onchange = () => {
      this.files = [];
      for (let index = 0; index < fileUpload.files.length; index++) {
        const file = fileUpload.files[index];
        this.files.push({data: file, inProgress: false, progress: 0});
      }
      this.uploadFiles();
    };
    fileUpload.click();
  }

  filterOnChange(name: string, variable: string, checked: boolean) {
    if (checked) {
      this.addToFilter(name, variable);
    } else {
      this.removeFromFilter(name, variable);
    }

    this.service.filter(this.filter).subscribe(result => {
      this.columns = this.getColumnsFromResult(result);
      this.getRowsFromResult(result);
      this.addLevelsToFiltered(this.columns, this.rows);
    });
  }

  private getRowsFromResult(result) {
    this.rows = [];
    this.rows.pop();
    for (let i = 2; i < result.length; i++) {
      this.rows.push(result[i]);
    }
  }

  private getColumnsFromResult(result) {
    this.columns = [];
    this.columns.pop();
    for (let i = 0; i < result[1].length; i++) {
      this.columns.push(result[1][i]);
    }
    return this.columns;
  }

  private removeFromFilter(name: string, variable: string) {
    for (let i = 0; i < this.filter.length; i++) {
      const filterNiveau = this.filter[i];
      const variables = filterNiveau.variables;
      const numberOfItemsToDelete = 1;
      if (filterNiveau.name === name) {
        const index = variables.indexOf(variable);
        variables.splice(index, numberOfItemsToDelete);
      }
      const empty = 0;
      if (variables.length === empty) {
        const index = this.filter.indexOf(filterNiveau);
        this.filter.splice(index, numberOfItemsToDelete);
      }
    }
  }

  private addToFilter(name: string, variable: string) {
    for (let i = 0; i < this.filter.length; i++) {
      const filterNiveau = this.filter[i];
      if (filterNiveau.name === name) {
        filterNiveau.variables.push(variable);
        return;
      }
    }
    const variables: string[] = [];
    variables.push(variable);
    const niveau: Level = {name, variables};
    this.filter.push(niveau);
  }


  desiredPropertyOnChange(property: PropertyExtractionScript, checked: boolean) {
    if (checked) {
      const notFound = -1;
      if (this.desiredProperties.indexOf(property) === notFound) {
        this.desiredProperties.push(property);
      }
    } else {
      const deleteNumberOfItems = 1;
      this.desiredProperties.splice(this.desiredProperties.indexOf(property), deleteNumberOfItems);
    }
  }

  executeScripts() {
    this.service.execute(this.filteredLevels, this.desiredProperties).subscribe(data => {
      console.log(data);
    });
  }


  private addLevelsToFiltered(columns: any[], rows: any[]) {
    for (let i = 0; i < rows.length; i++) {
      const row = rows[i];
      const rowSize = row[i].length;
      const filteredRowSet = [];
      for (let j = 0; j < rowSize; j++) {
        const level: Level = {name: columns[j], variables: row[i][j]};
        filteredRowSet.push(level);
      }
      this.filteredLevels.push(filteredRowSet);
    }
  }
}
