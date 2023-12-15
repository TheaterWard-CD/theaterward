import 'dart:async';

import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';

import 'package:flutter_gl/flutter_gl.dart';
import 'package:three_dart/three_dart.dart' as THREE;
import 'package:three_dart_jsm/three_dart_jsm.dart' as THREE_JSM;


class Character extends StatefulWidget {
  int no = 0;
  Character({super.key, required int seatNo}) {
    no = seatNo;
  }

  @override
  createState() => CharacterState();
}

class CharacterState extends State<Character> {
  final TextEditingController inputController = TextEditingController();
  late double width;
  late double height;
  Map<String, dynamic> animationsMap = {};
  bool loaded = false;
  String transcriptText = "";

  late FlutterGlPlugin three3dRender;
  late THREE.WebGLRenderer renderer;
  late THREE.AnimationAction action;
  Size? screenSize;
  late THREE.Scene scene;
  late THREE.Camera camera;
  late THREE.AnimationMixer mixer;
  THREE.Clock clock = THREE.Clock();
  late THREE_JSM.OrbitControls controls;
  double dpr = 1.0;
  bool disposed = false;
  late THREE.WebGLMultisampleRenderTarget renderTarget;
  dynamic sourceTexture;
  late THREE.Object3D model;
  final GlobalKey<THREE_JSM.DomLikeListenableState> _globalKey =
  GlobalKey<THREE_JSM.DomLikeListenableState>();

  @override
  void initState() {
    super.initState();
  }

  initSize(BuildContext context) {
    if (screenSize != null) {
      return;
    }

    final mqd = MediaQuery.of(context);

    screenSize = mqd.size;
    dpr = mqd.devicePixelRatio;

    initPlatformState();
  }

  // Platform messages are asynchronous, so we initialize in an async method.
  Future<void> initPlatformState() async {
    width = screenSize!.width;
    height = screenSize!.height;
    // remove appbar height
    height -= kToolbarHeight;

    three3dRender = FlutterGlPlugin();

    Map<String, dynamic> options = {
      "antialias": true,
      "alpha": false,
      "width": width.toInt(),
      "height": height.toInt(),
      "dpr": dpr
    };

    await three3dRender.initialize(options: options);

    setState(() {});

    Future.delayed(const Duration(milliseconds: 100), () async {
      await three3dRender.prepareContext();
      initScene();
    });
  }

  @override
  Widget build(BuildContext context) {
    return Builder(
      builder: (BuildContext context) {
        initSize(context);
        return SingleChildScrollView(child: _build(context));
      },
    );
  }

  Widget _build(BuildContext context) {
    return Column(
      children: [
        Stack(
          children: [
            _characterBuild(),
          ],
        ),
      ],
    );
  }

  Widget _characterBuild() {
    return THREE_JSM.DomLikeListenable(
      key: _globalKey,
      builder: (BuildContext conetxt) {
        return SizedBox(
          width: width,
          height: height - 30,
          child: Builder(
            builder: (BuildContext context) {
              if (!loaded) {
                return const SizedBox(
                  height: 50,
                  width: 50,
                  child: Center(
                    child: CircularProgressIndicator(
                      valueColor:
                      AlwaysStoppedAnimation<Color>(Colors.red),
                    ),
                  ),
                );
              }
              if (kIsWeb) {
                return three3dRender.isInitialized
                    ? HtmlElementView(
                    viewType: three3dRender.textureId!.toString())
                    : Container();
              } else {
                return three3dRender.isInitialized
                    ? Texture(textureId: three3dRender.textureId!)
                    : Container();
              }
            },
          ),
        );
      },
    );
  }

  render() {
    final gl = three3dRender.gl;
    renderer.render(scene, camera);
    gl.flush();

    if (!kIsWeb) {
      three3dRender.updateTexture(sourceTexture);
    }
  }

  initRenderer() {
    Map<String, dynamic> options = {
      "width": width,
      "height": height,
      "gl": three3dRender.gl,
      "antialias": true,
      "canvas": three3dRender.element
    };
    renderer = THREE.WebGLRenderer(options);
    renderer.setPixelRatio(dpr);
    renderer.setSize(width, height, false);
    renderer.shadowMap.enabled = false;

    if (!kIsWeb) {
      var pars = THREE.WebGLRenderTargetOptions({"format": THREE.RGBAFormat});
      renderTarget = THREE.WebGLMultisampleRenderTarget(
          (width * dpr).toInt(), (height * dpr).toInt(), pars);
      renderTarget.samples = 4;
      renderer.setRenderTarget(renderTarget);
      sourceTexture = renderer.getRenderTargetGLTexture(renderTarget);
    }
  }

  initScene() {
    initRenderer();
    initPage();
  }

  initPage() async {
    // setup camera
    camera = THREE.PerspectiveCamera();
    //camera.position.set(2, 2, 12); //2,2,12

    // scene
    scene = THREE.Scene();

    // lights setup
    var pmremGenerator = THREE.PMREMGenerator(renderer);
    scene.background = THREE.Color.fromHex(0xFFfafafa);
    scene.environment =
        pmremGenerator.fromScene(THREE_JSM.RoomEnvironment()).texture;

    var light = THREE.AmbientLight(0xffffff,10);
    scene.add(light);

    //var pointLight = THREE.PointLight(0xffffff, 0.8);
    //camera.add(pointLight);

    // load model
    var loader = THREE_JSM.GLTFLoader(null).setPath('assets/');
    var result = await loader.loadAsync('bluesquare_adddata.glb');

    model = result["scene"];

    String formatted = widget.no.toString().padLeft(3, "0");
    var nowPos = model.getObjectByName('\uc2e4\ub9b0\ub354$formatted')?.getWorldPosition(null); // \ud050\ube0c.610
    if (nowPos != null) {
      camera.position.set(nowPos.x, nowPos.y + 3, nowPos.z);
    }
    var stagePos = model.getObjectByName('Stage')?.getWorldPosition(null);
    if (stagePos != null) {
      camera.lookAt(THREE.Vector3(stagePos.x, stagePos.y, stagePos.z));
    }
    debugPrint(" load gltf success model: $model");


    // controls
    controls = THREE_JSM.OrbitControls(camera, _globalKey);
    controls.enableDamping =
    true; // an animation loop is required when either damping or auto-rotation are enabled
    controls.dampingFactor = 0.05;

    controls.screenSpacePanning = false;
    controls.maxPolarAngle = THREE.Math.PI / 2;
    controls.target.set(stagePos!.x, stagePos.y, stagePos.z);

    //model.position.set(0, -2.5, 0); //0,-2.5,0
    //set rotation
    //model.rotation.set(0, 0.20, 0); // 0,0,0
    //model.scale.set(3, 3, 3);
    //set zooming
    //camera.zoom = 1.3;
    camera.updateProjectionMatrix();

    scene.add(camera);
    scene.add(model);

    mixer = THREE.AnimationMixer(model);

    // clip.name to get name of animation
    for (var i = 0; i < result["animations"].length; i++) {
      THREE.AnimationClip animationClip = result["animations"][i];
      animationsMap[animationClip.name.toLowerCase()] = animationClip;
    }

    //print all animations names
    print(animationsMap.keys);
    setState(() => loaded = true);
    animate();

  }

  animate() {
    if (!mounted || disposed) {
      return;
    }
    if (!loaded) {
      return;
    }
    var delta = clock.getDelta();
    mixer.update(delta);
    controls.update();
    render();

    Future.delayed(const Duration(milliseconds: 40), () {
      animate();
    });
  }

  @override
  void dispose() {
    debugPrint(" dispose ............. ");
    THREE.loading = {};
    disposed = true;
    three3dRender.dispose();

    super.dispose();
  }
}