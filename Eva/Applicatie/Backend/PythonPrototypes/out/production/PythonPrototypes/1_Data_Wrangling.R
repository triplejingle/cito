
# https://unicode.org/emoji/charts/full-emoji-list.html
require(reshape2)
txt <- readLines("Annemieke.txt", encoding = "UTF-8")
txt <- txt[-1]

# Extract timestamp
timestamp <- as.POSIXct(substr(txt, 1, 17), format = "%d/%m/%Y, %H:%M")

# Extract author
author <- regmatches(txt, regexpr("(?<=- )([A-z0-9_ ]*)(?=:)", txt, perl = TRUE)) 

# Extract messages
message <- regmatches(txt[1], regexpr("(?<=: )(.*)", txt[1], perl = TRUE))

# create dataframe
dat <- data.frame(timestamp, author, message)

save(dat, file = "dat.Rdata")
