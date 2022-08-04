# Welcome to Workshop 07 - Intro to R.

# Today we'll be learning the basics of R as suggested by Hadley Wickham
# https://gist.github.com/hadley/6734639

# For this lecture, we will familiarize and practice several topics:

###############################################################################
# what is R
###############################################################################

###############################################################################
# IDE of choice and what do things do in RStudio
###############################################################################

###############################################################################
# variable assignment 
# and basic data types  (character, double, integer, logical)
# and type casting
###############################################################################
aCharacter <- "a"
alsoACharacter <- "hello everyone"

type("aCharacter")

x <- "3"
x <- as.numeric(x)

y <- 3.0
y <- as.character(y)

x <- TRUE
x <- T

x <- FALSE
x <- F


###############################################################################
# basic data structures (vector, matrix, list, data frame)
###############################################################################
# quick example
aQuickVector <- c(3,4,5,6,1,2,3)
anotherQuickVector <- c("a", "b", "c", "d")

# what about this vector?
anotherVector <- c("a", TRUE, 3)

c(TRUE, 5)
c(FALSE, 3)

# numeric vector
tmpVectorA <- c(1:10)
tmpVectorB <- c(10:1)

# accessing vector contents (remember index splicing?)
tmpVectorA[1] # what do you think this gets?
tmpVectorA[3]

tmpVectorB[1:4]
tmpVectorB[c(1,3,5)]

# named vector (equivalent to dictionaries in python)
tmpVectorC <- c("bob" = 3, "jessie" = 1, "anna" = 15)
tmpVectorC[1]
tmpVectorC["bob"]

names(tmpVectorC) <- c("jake", "jayme", "betu")

length()

# matrix
myMatrix <- matrix(c(1:10), nrow = 2, ncol = 5)

# data frame
myDF <- data.frame(
  colA = c(3,4,5,6),
  colB = c("CD3", "CD8", "CD16", "CD95")
)

myDF2 <- data.frame(
  colA = c(3,4,5,6),
  colB = c("CD3", "CD8", "CD16", "CD95")
)

# changing names
colnames()
rownames()
dim()
nrow()
ncol()

# accessing data frame
# [row, index]
# [, "colname"]
# [, c(1:2)]
# myDF2$colname

# lists can hold different types of stuff including itself
tmpList <- list(
  "A" = myDF,
  "B" = myDF2,
  "C" = 3
)

# accessing list contents
# []
# [[]]


###############################################################################
# what is NULL?
###############################################################################
typeof(NULL)
class(NULL)

# from r documentation
# https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/NULL

# NULL represents the null object in R:
# it is a reserved word. NULL is often returned by expressions and functions whose value is undefined.

###############################################################################
# what is a factor?
###############################################################################

# from r documentation
# https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/factor

myFriends <- c("p20", "p200", "p2", "p10")
myFriends <- factor(myFriends)

myFriends

# factor returns an object of class "factor" which has a set of integer codes the length of x
# with a "levels" attribute of mode character and unique (!anyDuplicated(.)) entries.
# If argument ordered is true (or ordered() is used) the result has class c("ordered", "factor").

###############################################################################
# comparison operators
# >, <, ==, <=, >=, !=
###############################################################################

###############################################################################
# boolean operators and the notion of short-circuiting
# &, &&, |, || 
###############################################################################
TRUE & TRUE

3 != 3 & TRUE

3 != 5 & FALSE

TRUE | FALSE

FALSE | TRUE

TRUE & FALSE | TRUE | TRUE & TRUE | FALSE

3 == 3 && 5 == 5

6 == 6 || 7 != 7

###############################################################################
# control flows: if/else statements
###############################################################################
x <- 1000

if (x > 1000 | x %% 99) {
  print("x is greater than 1000 or divisible by 99")
} else if (x > 100) {
  print("x is greater than 100")
} else {
  print("who am i any more")
}

###############################################################################
# control flows: for loops
###############################################################################

for (i in seq(1, 10, 1)) {
  print(i)
}

myFriends <- c("p20", "p200", "p2", "p10")
for (i in myFriends) {
  print(i)
}

###############################################################################
# modularity: functions
###############################################################################


###############################################################################
# control flows: apply family: sapply and lapply
###############################################################################
# lapply returns a list
# sapply returns a vector

myDF2 <- data.frame(
  colA = c(3,4,5,6),
  colB = c("CD3", "CD8", "CD16", "CD95")
)

myDF2$colC <- sapply(seq_along(colA), function(x) {
  print(x)
  return(x + 1)
})

myDF2


###############################################################################
# input/output
###############################################################################
# read.csv()
df <- read.csv("practiceReadingMe.tsv", sep = "\t")
df

for (i in c(2:4)) {
  df[, i] <- df[, i] / 100
}

# write.csv()
write.table(df, "practiceWritingMe.tsv", sep = "\t", row.names = FALSE, col.names = TRUE, quote = FALSE)


