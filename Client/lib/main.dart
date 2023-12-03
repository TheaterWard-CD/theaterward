import 'dart:async';
import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:theaterward/models/user_model.dart';
import 'package:theaterward/models/login_model.dart';
import 'package:theaterward/models/show_model.dart';
import 'package:theaterward/screens/search_screen.dart';
import 'package:provider/provider.dart';
import 'package:http/http.dart' as http;

import 'package:theaterward/models/theater_model.dart';
import 'package:theaterward/screens/theater_screen.dart';

void main() {
  final String URL = "http://3.35.3.49/api/";
  final request = Uri.parse(URL + "theater");
  var jsonResponse;

  Future<dynamic> fetch() async {
    final response = await http.get(request);
    jsonResponse = jsonDecode(utf8.decode(response.bodyBytes));
    print(jsonResponse);
  }
  fetch();
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Theater Ward',
      routes: {
        '/': (context) => SplashScreen(),
        '/login': (context) => LoginScreen(),
        '/search': (context) => SearchScreen(),
        //'/theater': (context) => TheaterScreen(),
        //'/seat': (context) => SeatScreen(),
      },
      theme: ThemeData(
        primaryColor: Colors.black,
        //colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      initialRoute: '/',
    );
  }
}


class SplashScreen extends StatefulWidget {
  const SplashScreen({super.key});

  @override
  State<SplashScreen> createState() => _SplashScreenState();
}

class _SplashScreenState extends State<SplashScreen> {
  @override
  void initState() {
    super.initState();
    Timer(
      const Duration(milliseconds: 1500),
        () => Navigator.of(context).pushReplacementNamed('/login'),
    );
  }

  Widget build(BuildContext context) {
    return Container(
      child: Row(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Text('Theater Ward'),
        ],
      )
    );
  }
}

class LoginScreen extends StatelessWidget {
  const LoginScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("로그인 화면"),
      ),
      body: Column(
        children: [
          IdInput(),
          PwInput(),
          LoginButton(),
          const Padding(
            padding: EdgeInsets.all(8.0),
            child: Divider(thickness: 1,),
          ),
          //RegisterButton(),
        ],
      ),
    );
  }
}

class IdInput extends StatelessWidget {
  const IdInput({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      child: TextField(
        onChanged: (id) {

        },
        keyboardType: TextInputType.text,
        decoration: const InputDecoration(
          labelText: 'ID'
        ),
      ),
    );
  }
}

class PwInput extends StatelessWidget {
  const PwInput({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      child: TextField(
        onChanged: (id) {

        },
        keyboardType: TextInputType.text,
        decoration: const InputDecoration(
            labelText: 'Password'
        ),
      ),
    );
  }
}

class LoginButton extends StatelessWidget {
  const LoginButton({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      width: MediaQuery.of(context).size.width,
      height: MediaQuery.of(context).size.height * 0.08,
      child: ElevatedButton(
        style: ElevatedButton.styleFrom(
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(30.0)
          )
        ),
        onPressed: () async {
          Navigator.pushReplacementNamed(context, '/search');
        },
        child: const Text('로그인'),
      ),
    );
  }
}

