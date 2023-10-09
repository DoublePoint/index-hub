<template>
  <div id="container"  class="app-container home">
    
  </div>
</template>

<script>
const THREE = require('three')
const OrbitControls = require('three-orbitcontrols')
export default {
  name: "webgl",
  data() {
    return {
      // 版本号
      version: "3.6.0",
    };
  },
  mounted(){
      init();
  },
  methods: {
    goTarget(href) {
      window.open(href, "_blank");
    },
  },
};
var scene, camera, renderer;

function init(){
    scene = new THREE.Scene();

    const geometry = new THREE.BoxGeometry( 1, 1, 1 );
    const material = new THREE.MeshBasicMaterial( {color: 0x00ff00} );
    const cube = new THREE.Mesh( geometry, material );
    scene.add( cube );


    //这里参数不懂的同学回去看基本知识里的camera部分
    camera = new THREE.PerspectiveCamera(90, document.body.clientWidth / document.body.clientHeight, 0.1, 100);
    //camera的位置在x0,y0,z3，还记得迪尔卡右手坐标系吗？
    camera.position.set(0, 0, 3);
    
    renderer = new THREE.WebGLRenderer();
    renderer.setSize(document.body.clientWidth, document.body.clientHeight);
    document.getElementById("container").appendChild(renderer.domElement);
    
    var controls = new THREE.OrbitControls(camera, renderer.domElement);

    //等待添加模型

    loop();
}

function loop() {
    requestAnimationFrame(loop);
    renderer.render(scene, camera);
}

</script>

<style scoped lang="scss">
.home {
  blockquote {
    padding: 10px 20px;
    margin: 0 0 20px;
    font-size: 17.5px;
    border-left: 5px solid #eee;
  }
  hr {
    margin-top: 20px;
    margin-bottom: 20px;
    border: 0;
    border-top: 1px solid #eee;
  }
  .col-item {
    margin-bottom: 20px;
  }

  ul {
    padding: 0;
    margin: 0;
  }

  font-family: "open sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 13px;
  color: #676a6c;
  overflow-x: hidden;

  ul {
    list-style-type: none;
  }

  h4 {
    margin-top: 0px;
  }

  h2 {
    margin-top: 10px;
    font-size: 26px;
    font-weight: 100;
  }

  p {
    margin-top: 10px;

    b {
      font-weight: 700;
    }
  }

  .update-log {
    ol {
      display: block;
      list-style-type: decimal;
      margin-block-start: 1em;
      margin-block-end: 1em;
      margin-inline-start: 0;
      margin-inline-end: 0;
      padding-inline-start: 40px;
    }
  }
}
</style>

