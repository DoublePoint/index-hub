<template>
  <div id="aid"  class="app-container home">
    
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
      document.getElementById("aid").appendChild(renderer.domElement);//
  },
  methods: {
    goTarget(href) {
      window.open(href, "_blank");
    },
  },
};
/**
   * 一：创建场景对象 Scene
   * 
   */

  var scene = new THREE.Scene();

  /**
   * 二：创建网格模型
   */
  /**
  * Sphere 球体    
  * Geometry 几何形状 
  * Meterial 材料
  * Mesh 网状物
  * lambert 亮度单位
  * Ambient 周围环境的
  * Orthographic 直角的
  *  */ 

  //var geometry = new THREE.SphereGeometry(60,40,40);//创建一个球体几何对象
  
  var geometry = new THREE.BoxGeometry(100,100,100);//创建一个立方体几何对象
  var material = new THREE.MeshLambertMaterial({
      color:0x00ffff,
      // wireframe:false,
      // specular:0x4488ee,
      // shininess:12
  });//材质对象
  var mesh = new THREE.Mesh(
      geometry,material
  );//网格模型对象
  scene.add(mesh);//网格模型添加到场景中


  var box = new THREE.SphereGeometry(60,40,40);
  var material2 = new THREE.MeshPhongMaterial({
      color:0x00ff00,
      specular:0x4488ee,
      shininess:12
  });//材质对象
  var mesh2 = new THREE.Mesh(
      box,material2
  );//网格模型对象
  mesh2.translateZ(-200)
  scene.add(mesh2);//网格模型添加到场景中


  /**
   * 三：光源设置
   */
  //点光源
  var point = new THREE.PointLight(0xffffff);
  point.position.set(400, 200, 300);//点光源的位置
  scene.add(point) //将点光源添加到场景中

  //环境光
  var ambient = new THREE.AmbientLight(0x444444);
  scene.add(ambient);

  //  console.log(scene);
  //  console.log(scene.children);
  /**
  * 四：相机设置
  */

  var width = window.innerWidth;//窗口宽度
  var height = window.innerHeight;//窗口高度
  var k = width / height;//窗口宽高比
  var s = 200;//三位场景显示范围控制系数，系数越大，显示的范围越大

  //创建相机对象
  var camera = new THREE.OrthographicCamera(-s*k,s*k,s,-s, 1,1000);
  camera.position.set(200,200,200);//设置相机位置
  camera.lookAt(scene.position);//设置相机方向（指向的场景方向）

  /**
   * 五：创建渲染器对象
   */
  var renderer = new THREE.WebGLRenderer();
  renderer.setSize(width,height);//设置渲染区域尺寸
  renderer.setClearColor(0xb9d3ff,1)//设置背景颜色

  renderer.render(scene,camera);

  
  // 辅助坐标系  参数250表示坐标系大小，可以根据场景大小去设置
  var axisHelper = new THREE.AxisHelper(250);
  scene.add(axisHelper);

  // let T0 = new Date();//上次时间
  // function render(){
  //     let T1 = new Date();//本次时间
  //     let t = T1-T0;//时间差
  //     T0 = T1;//把本次时间赋值给上次时间
  //     requestAnimationFrame(render);
  //     renderer.render(scene,camera);//执行渲染操作
  //     mesh.rotateY(0.001*t);//旋转角速度0.001弧度每毫秒
  // }
  // setInterval("render()",20);
  // render();
  function render(){
      renderer.render(scene,camera)
  }
  render();
  var controls = new THREE.OrbitControls(camera,renderer.domElement);//创建控件对象
  controls.addEventListener('change', render);//监听鼠标、键盘事件

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

