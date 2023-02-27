import './App.css';
import React, { useRef, useState } from 'react';
import * as THREE from 'three'
import { Canvas } from '@react-three/fiber';
import { OrbitControls } from '@react-three/drei';
import Character from './Character.js';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader';

function App() {
  const canvas = useRef()
  // 1. 장면 만들기 
  let scene = new THREE.Scene()
  // 2. 브라우저에 렌더링
  // 3D 요소를 웹 브라우저에 보여주려고 할 경우 WebGL 를 사용한다고 함 
  let renderer = new THREE.WebGLRenderer({
    // 웹 브라우저 어디에 보여줄지는 여기서 지정
    canvas: document.getElementById('canvas')
  })

  // 3D model을 보여줄 때 필요한 것들
  // 1.카메라, 2.조명, 3.배경
  
  //  PerspectiveCamera = 원근법, OrthographicCamera = 원근법 X
  let camera = new THREE.PerspectiveCamera(30,1)

  // 다운받은 것을(gltf파일의 경우) 보여주고자 할 경우
  let loader = new GLTFLoader()
  loader.load('scene.gltf', function(gltf) {
    scene.add(gltf.scene)
    renderer.render(scene, camera)
  })
  return (
    <div className="App">
      <canvas ref={canvas} id='canvas' width={300} height={300}>
      
      </canvas>
    </div>
  );
}

export default App;
