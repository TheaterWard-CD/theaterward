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
        () => Navigator.of(context).pushReplacementNamed('/search'),
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
