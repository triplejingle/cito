import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AnalyserenAntwoordComponent } from './analyseren-antwoord.component';

describe('AnalyserenAntwoordComponent', () => {
  let component: AnalyserenAntwoordComponent;
  let fixture: ComponentFixture<AnalyserenAntwoordComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AnalyserenAntwoordComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AnalyserenAntwoordComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
