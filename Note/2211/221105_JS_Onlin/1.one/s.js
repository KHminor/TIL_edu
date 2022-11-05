const participantNums =  [[1, 3, 2, 2, 1], 
[3, 7, 100, 21, 13, 6, 5, 7, 5, 6, 3, 13, 21],
[9, 1, 8, 7, 71, 33, 62, 35, 11, 4, 7, 71, 33, 8, 9, 1, 4, 11, 35]
]


participantNums.forEach((arr) => {
  for (num of arr) {
    let numlist = []
    for (a of arr) {
      if (num === a) {
        numlist.push(a)
      }
    }
    if (!(numlist.length === 2)) {
      console.log(num);
    }
  }
})

// 3
// 100
// 62