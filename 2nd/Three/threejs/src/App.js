import './App.css';
import React, { useState } from 'react';
import * as THREE from 'three'
import { Canvas } from '@react-three/fiber';
import { OrbitControls } from '@react-three/drei';

function App() {

  const [click, setClick] = useState(false)
  const [hover, setHover] = useState(false)
  return (
    <div className="App">
      <Canvas>
        <OrbitControls autoRotate={true}/>
        <mesh onClick={()=> {setClick(!click)}} 
              onPointerOver={()=> {setHover(!hover)}}
              onPointerOut={()=> {setHover(!hover)}}
              scale={hover? 1.5: 1}
              
            >
        <spotLight position={[10, 10, 10]} angle={0.15} penumbra={1} />
          <ambientLight intensity={1}/>
          <pointLight position={[10, 10, 10]} />
          <boxGeometry  args={[1, 1, 1]}/>
          <meshStandardMaterial attach="material" color={click? 'pink': 0xa3b18a}
            
          />
        </mesh>
        {/* <mesh rotation={[90, 90, 8]}>
          <boxBufferGeometry attach="geometry" args={[1, 1, 1]} />
          <meshLambertMaterial attach="material" color="blue" />
        </mesh> */}
      </Canvas>
    </div>
  );
}

export default App;
