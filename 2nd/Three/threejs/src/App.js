import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader';
import * as THREE from 'three';
import { useEffect, useRef } from 'react';

function MyCanvas() {
  const canvasRef = useRef(null);

  useEffect(() => {
    let scene = new THREE.Scene();
    let renderer = new THREE.WebGLRenderer({
      canvas: canvasRef.current,
      antialias: true,
    });
    renderer.outputEncoding = THREE.sRGBEncoding;
    let camera = new THREE.PerspectiveCamera(30, 1);
    camera.position.set(0, 0, 1000);
    scene.background = new THREE.Color('#c9f0ff');
    let light = new THREE.DirectionalLight(0xffffff, 1.4);
    let light1 = new THREE.AmbientLight(0xffffff);
    light.position.set(100, 50, 50);
    scene.add(light, light1);

    let loader = new GLTFLoader();
    loader.load('pusheen/scene.gltf', function (gltf) {
      scene.add(gltf.scene);
      function animate() {
        requestAnimationFrame(animate);
        gltf.scene.rotation.y -= 0.01;
        renderer.render(scene, camera);
      }
      animate();
    });
  }, []);

  return <canvas ref={canvasRef} width={400} height={400} />;
}

export default function App() {
  return (
    <div>
      <MyCanvas />
    </div>
  );
}




