import * as THREE from '../build/three.module.js'

class App {
	constructor () {
		const divContainer = document.querySelector('#webgl-container');
		// 밑줄이 있는 변수(필드 객체) 또는 메서드는 해당 앱 클래스 내부에서만 사용하는 프라이빗 변수, 메서드인데
		// JS에는 그런게 없기에 개발자들 간의 약속이라고 한다.
		this._divContainer = divContainer;

		const renderer = new THREE.WebGLRenderer({ antialias: true})
		renderer.setPixelRatio(window.devicePixelRatio)
		divContainer.appendChild(renderer.domElement);
		this._renderer = renderer;

		const scene = new THREE.Scene()
		this._scene = scene

		this._setupCamera()
		this._setupLight()
		this._setupModel()

		window.onresize = this.resize.bind(this);
		this.resize()

		requestAnimationFrame(this.render.bind(this))

	}

	_setupCamera() {
		const width = this._divContainer.clientWidth
		const height = this._divContainer.clientHeight
		const camera = new THREE.PerspectiveCamera(
			75,
			width/height,
			0.1,
			100
		)
		camera.position.z = 2
		this._camera = camera
	}

	_setupLight() {
		const color = 0xffffff
		const intensity = 1
		const light = new THREE.DirectionalLight(color, intensity)
		light.position.set(-1, 2, 4)
		this._scene.add(light)
	}

	_setupModel() {
		// 정육면체 생성 (가로, 세로, 깊이)
		const geometry = new THREE.BoxGeometry(1, 1, 1)
		// 파란색 계열로 생성
		const material = new THREE.MeshPhongMaterial({color: 0x44a88})

		// Mesh() 큐브를 생성
		const cube = new THREE.Mesh(geometry, material)

		this._scene.add(cube)
		this._cube = cube
	}


	resize() {
		// 해당 태그의 크기를 얻어와서
		const width = this._divContainer.clientWidth
		const height = this._divContainer.clientHeight

		// 화면을 설정
		this._camera.aspect = width/height
		this._camera.updateProjectionMatrix()

		this._renderer.setSize(width, height)
	}

	render(time) {
		// 렌더러가 신을 카메라의 시점에 따라 렌더하라는 의미
		this._renderer.render(this._scene, this._camera)
		this.update(time)
		requestAnimationFrame(this.render.bind(this))
	}

	update(time) {
		// second time
		time *= 0.001
		this._cube.rotation.x = time
		this._cube.rotation.y = time
	}
}



window.onload = function () {
	new App()
}
