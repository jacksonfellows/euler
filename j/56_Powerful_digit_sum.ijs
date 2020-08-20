digits =: 10 & #.inv
digitSum =: +/"1 @: digits
p56 =: >./ digitSum , (i.100x) ^/ (i.100x)
