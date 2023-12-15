//package com.abcd.theaterward.controller;
//
//import com.abcd.theaterward.domain.JwtAuthenticationResponse;
//import com.abcd.theaterward.domain.SignInRequest;
//import com.abcd.theaterward.domain.SignUpRequest;
//import com.abcd.theaterward.domain.Users;
//import com.abcd.theaterward.service.AuthenticationService;
//import org.springframework.http.ResponseEntity;
//import org.springframework.web.bind.annotation.PostMapping;
//import org.springframework.web.bind.annotation.RequestBody;
//import org.springframework.web.bind.annotation.RequestMapping;
//import org.springframework.web.bind.annotation.RestController;
//
//@RestController
//@RequestMapping("/api/auth")
//public class AuthenticationController {
//    private final AuthenticationService authenticationService;
//
//    public AuthenticationController(AuthenticationService authenticationService) {
//        this.authenticationService = authenticationService;
//    }
//
//
//    @PostMapping("/signup")
//    public ResponseEntity<Users> signup(@RequestBody SignUpRequest signUpRequest) {
//        return ResponseEntity.ok(authenticationService.signup(signUpRequest));
//    }
//
//
//    @PostMapping("/signin")
//    public ResponseEntity<JwtAuthenticationResponse> signin(@RequestBody SignInRequest signInRequest) {
//        return ResponseEntity.ok(authenticationService.signin(signInRequest));
//    }
//}
