import './App.css';
import React, {
  useEffect,
  useState
} from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {
  items,
  datas
} from './data.js'
import {
  Routes,
  Route,
  Link,
  useNavigate,
  Outlet
} from 'react-router-dom';
import comp from './newcomponent'
import {
  Navbar,
  Nav
} from 'react-bootstrap';
import Detail from './Detail'
import axios from 'axios'
import Cart from './routes/Cart'
import {
  useQuery
} from '@tanstack/react-query';

function App() {

  // // local Storage에 array 또는 object 저장해보기 (JSON 형태)
  // let obj = {name: 'kim'}
  // localStorage.setItem('data', JSON.stringify(obj))

  // //저장된 데이터를 꺼내보기
  // let d = localStorage.getItem('data')
  // console.log(d);

  // // 저장된 데이터를 JSON-> array/object로 변환 후 출력
  // console.log(JSON.parse(d));
  // console.log(JSON.parse(d).name);

  useEffect(() => {
    let checkLocal = localStorage.getItem('watched')
    if (!(JSON.parse(checkLocal))) {
      localStorage.setItem('watched', JSON.stringify([]))
    }
  }, [])

  let navigate = useNavigate()
  let [item, setItems] = useState(items)
  let [data, setDatas] = useState(datas)
  let [axiosData, setaxiosData] = useState()
  let [btnClick, setBtnClick] = useState(0)
  let [loading, setLoading] = useState(false)

  let result = useQuery(['작명'], () => {
    return axios({
        url: 'https://codingapple1.github.io/userdata.json'
      })
      .then((a) => {
        console.log('요청됨');
        return a.data
      })
      .catch((e) => {
        return e
      })

  }, {
    staleTime: 2000
  })

  // console.log(result.data);
  // console.log(result.isFetching);
  // console.log(result.error);

  return ( <
      div className = "App" >

      {
        /* navbar */ } <
      Navbar id = 'navbar'
      variant = "dark" > {
        /* <div className="subfont"> */ } <
      div className = 'grid' >
      <
      div > < /div> <
      Nav style = {
        {
          color: 'black',
          justifyContent: 'center',
          alignItems: 'center'
        }
      }
      href = "#home" > < span class = "material-symbols-outlined"
      style = {
        {
          marginRight: '3px'
        }
      } > menu < /span>메뉴</Nav >
      <
      div > < /div> <
      Nav style = {
        {
          color: 'black',
          justifyContent: 'center',
          alignItems: 'center'
        }
      }
      href = "#features" > < span class = "material-symbols-outlined" > search < /span>검색</Nav >
      <
      div > < /div> <
      Nav className = 'mainfont'
      style = {
        {
          color: 'black',
          justifyContent: 'center',
          alignItems: 'center',
          fontSize: '2rem',
          letterSpacing: '5px',
          cursor: 'pointer'
        }
      }
      onClick = {
        () => {
          navigate('/')
        }
      } > LOUIS VUITTON < /Nav> <
      div > < /div> <
      Nav style = {
        {
          color: 'black',
          justifyContent: 'center',
          alignItems: 'center',
          cursor: 'pointer'
        }
      }
      onClick = {
        () => {
          navigate('/detail/0')
        }
      } > 위시리스트 < /Nav> <
      div > < /div> <
      Nav style = {
        {
          color: 'black',
          justifyContent: 'center',
          alignItems: 'center',
          cursor: 'pointer'
        }
      }
      onClick = {
        () => {
          navigate('/detail/1')
        }
      } > My lv < /Nav> <
      div > < /div> <
      Nav style = {
        {
          color: 'black',
          justifyContent: 'center',
          alignItems: 'center',
          cursor: 'pointer'
        }
      }
      href = "#pricing"
      onClick = {
        () => {
          navigate('/cart')
        }
      } > < span class = "material-symbols-outlined" > shopping_cart_checkout < /span></Nav >
      <
      div > < /div> {
        /* </div> */ } <
      /div> <
      /Navbar> <
      Nav className = 'ms-auto' > {
        result.isLoading ? '로딩중...' : result.data.name
      } < /Nav> {
        /* <Link style={{textDecoration: 'none', color:'black'}} to={'/'}>홈 </Link><br />
              <Link to={'/detail'}>상세페이지</Link><br />
              <Link to={'/comp'}>새로운 컴포넌트</Link> */
      }

      <
      Routes >
      <
      Route path = '/'
      element = {
        < >
        <
        div className = 'main-bg' > {
          /* 배경사진 */ } <
        /div> <
        div >
        <
        button onClick = {
          () => {
            setLoading(true)
            let urlNum = 2 + btnClick
            console.log(urlNum);
            axios.get('https://codingapple1.github.io/shop/data' + urlNum + '.json')
              .then((d) => {
                setLoading(false)
                setBtnClick(btnClick + 1)
                let newData = [...data, ...d.data]
                console.log(newData);
                setDatas(newData)
              })
              .catch((error) => {
                alert('상품이 더이상 없습니다(❁´◡`❁)')
                console.log(error)
              })
          }
        } > 버튼 < /button> <
        /div> <
        />} / >

        <
        Route path = '/detail/:id'
        element = {
          < Detail datas = {
            datas
          }
          />}/ >
          <
          Route path = '/comp'
          element = {
            < > {
              comp
            } <
            />}/ >

            <
            Route path = 'event'
            element = {
              < > < Event / > < />}> <
              Route path = 'one'
              element = {
                < > < p > 첫 주문시 양배추즙 서비스 < /p></ >
              }
              /> <
              Route path = 'two'
              element = {
                < > < p > 생일기념 쿠폰받기 < /p></ >
              }
              /> <
              /Route>

              <
              Route path = '/cart'
              element = {
                < > < Cart / > < />}>

                <
                /Route>

                <
                Route path = '*'
                element = {
                  < > 여긴 뭐하러 왔어 ? < />}/ >
                  <
                  /Routes>

                  <
                  div > {
                    loading === true ? < Loding / > : null
                  } <
                  /div>

                  <
                  div style = {
                    {
                      display: 'grid',
                      gridTemplateColumns: '1fr 1fr 1fr'
                    }
                  } > {
                    data.map((data) => {
                      return ( <
                        div onClick = {
                          () => {
                            navigate(`/detail/${data.id}`)
                          }
                        } >
                        <
                        Datas data = {
                          data
                        }
                        /> <
                        /div>  
                      )
                    })
                  } <
                  /div>

                  <
                  /div>
                );
              }

              function Event() {
                return ( <
                  div >
                  <
                  h4 > 오늘의 이벤트 < /h4> <
                  Outlet > < /Outlet> <
                  /div>
                )
              }

              function Datas(props) {
                // console.log(props);
                let dataId = props.data.id + 1
                return ( <
                  div style = {
                    {
                      display: 'flex',
                      justifyContent: 'center',
                      alignItems: 'center'
                    }
                  } >
                  <
                  div style = {
                    {
                      marginRight: '4px'
                    }
                  } >
                  <
                  img className = 'items'
                  style = {
                    {
                      height: '50%'
                    }
                  }
                  src = {
                    'https://codingapple1.github.io/shop/shoes' + dataId + '.jpg'
                  }
                  alt = "" / >
                  <
                  p style = {
                    {
                      marginTop: '7px'
                    }
                  } > {
                    props.data.title
                  } < /p> <
                  p > {
                    props.data.content
                  } < /p> <
                  p > {
                    props.data.price
                  } < /p> <
                  /div> <
                  /div>
                )
              }

              function Loding() {
                return ( <
                  div style = {
                    {
                      display: 'flex',
                      justifyContent: 'center',
                      alignItems: 'center'
                    }
                  } >
                  <
                  img src = "https://mblogthumb-phinf.pstatic.net/MjAyMDExMTJfMTgg/MDAxNjA1MTkxMjUwMzk4.BW7kx0zOQyxI57lwIxcYu40P1uicXhVNXQRSGegLuugg.RLMpOQkNfd72xWh8CJFLQz4ZwyGuZmWrDSdH8dfzArUg.GIF.bom____bom/90s_gif_(17).gif?type=w800"
                  alt = "" / >
                  <
                  /div>
                )
              }

              export default App;