import 'package:flutter/material.dart';

class LoginModel extends ChangeNotifier {
  String id = "";
  String pw = "";

  void setId(String id) {
    this.id = id;
    notifyListeners();
  }

  void setPw(String pw) {
    this.pw = pw;
    notifyListeners();
  }
}