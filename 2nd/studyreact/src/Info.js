import {useReducer} from 'react'

function reducer(state, action) {
  return {
    ...state,
    [action.name]: action.value
  }
}

const Info = () => {
  const [state, dispatch] = useReducer(reducer, {
    name: '', 
    nickname: ''
  })

  const {name, nickname} = state
  const onChange = e => {
    dispatch(e.target)
  }

  return (
    <div>
      <div>
        <div><input type="text" name='name' value={name} onChange={onChange}/></div>
        <div><input type="text" name='nickname' value={nickname} onChange={onChange}/></div>
      </div>
      <div>
        {name}
      </div>
      <div>
        {nickname}
      </div>
    </div>
  )
}
export default Info