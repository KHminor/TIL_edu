/*
Auto-generated by: https://github.com/pmndrs/gltfjsx
*/

import React, { useRef } from 'react'
import { useGLTF } from '@react-three/drei'

export function Model(props) {
  const { nodes, materials } = useGLTF('/test2.gltf')
  return (
    <group {...props} dispose={null}>
      <mesh geometry={nodes.UTails.geometry} material={materials.M_UTails} rotation={[Math.PI / 2, 0, 0]} />
    </group>
  )
}

useGLTF.preload('/test2.gltf')