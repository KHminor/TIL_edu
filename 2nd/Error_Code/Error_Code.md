React

하나의 click method 에서 여러 target 에 대한 처리를 조건에 따라 처리할 경우 
일반적으로 e.target을 하나의 target으로 묶어서 처리를 했지만

예를 들어 처리를 한번만 해야하는데 두번씩 처리가 되어 toast나 log 가 두번씩 찍힌다면 

e.target이 아니라 e.currentTarget을 각각의 요소에 넣어줘야 한다.

**오류**

```react
const click:MouseEventHandler<HTMLDivElement> = (e) => {
    const target = e.target as HTMLElement
    if (target.ariaLabel === '정보수정') {
      setIsClick(!isClick)
    } else if (e.currentTarget.ariaLabel === '변경') {
      console.log('두번 실행되나?');
      e.preventDefault()
      const data:any = {
        nickname: changeNickname,
        username: userId
      }
      nameCheckMutation(data).unwrap().then((r:any)=> {
        // console.log(r.data);
        if (r.data === false) {
          console.log('hi');
          setShowErrorMessage(true) // set showErrorMessage to true instead of calling toast.error directly
        }
      })
    }
    else if (e.currentTarget === ref.current) {
      console.log('hi');
      setIsClick(false)
    }
  }
```

**성공**

```react
const click:MouseEventHandler<HTMLDivElement> = (e) => {
    // const target = e.target as HTMLElement
    if (e.currentTarget.ariaLabel === '정보수정') {
      setIsClick(!isClick)
    } else if (e.currentTarget.ariaLabel === '변경') {
      console.log('두번 실행되나?');
      e.preventDefault()
      const data:any = {
        nickname: changeNickname,
        username: userId
      }
      nameCheckMutation(data).unwrap().then((r:any)=> {
        // console.log(r.data);
        if (r.data === false) {
          console.log('hi');
          setShowErrorMessage(true) // set showErrorMessage to true instead of calling toast.error directly
        }
      })
    }
    else if (e.target === ref.current) {
      console.log('hi');
      setIsClick(false)
    }
  }
```

