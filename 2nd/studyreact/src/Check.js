import { useState } from "react"
import styled, {css} from 'styled-components'

const Botton = styled.button`
  width: 2rem;
  height: 2rem;
  background-color: ${props => props.color || 'red'};
  transition: all 0.5s;
  &:hover {
    background-color: chocolate;
  }
  ${props => props.tt && css`
    &:hover {
      background-color: aquamarine;
    }
  `}
`

const Box = styled.div`
  background-color: ${props => props.color || 'blue'};
  padding: 1rem;
  display: flex;
  width: 1024px;
  margin: 0 auto;

  @media (max-width: 1024px) {
    width: 768px;
  }
  @media (max-width: 768px) {
    width: 100%;
  }

`

const Check = () => {
  const [state,setState] = useState({
    name: '',
    nickname: ''
  })
  const {name, nickname} = state

  const onChange = e => {
    const nextState = {
      ...state,
      [e.target.name]: e.target.value
    }
    setState(nextState)
  }
  
  return (
    <div>
      <div>
        <b>name:</b>{name}
      </div>
      <div>
        <b>nickname:</b>{nickname}
      </div>
      <Botton color="rgb(122,3,255)" tt={true}/>
      <Box />
      <div>
        <input type="text" onChange={onChange} value={name} name="name"/>
      </div>
      <div>
        <input type="text" onChange={onChange} value={nickname} name="nickname"/>
      </div>
    </div>
  )
  
}
export default Check