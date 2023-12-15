//package com.abcd.theaterward.service;
//
//import com.abcd.theaterward.domain.*;
//import com.abcd.theaterward.repository.JpaUserRepository;
//import org.springframework.security.authentication.AuthenticationManager;
//import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
//import org.springframework.security.core.userdetails.UserDetails;
//import org.springframework.security.crypto.password.PasswordEncoder;
//import org.springframework.stereotype.Service;
//
//@Service
//public class AuthenticationService {
//    private final JpaUserRepository jpaUserRepository;
//    private final PasswordEncoder passwordEncoder;
//    private final AuthenticationManager authenticationManager;
//    private final JwtService jwtService;
//
//    public AuthenticationService(JpaUserRepository jpaUserRepository, PasswordEncoder passwordEncoder, AuthenticationManager authenticationManager, JwtService jwtService) {
//        this.jpaUserRepository = jpaUserRepository;
//        this.passwordEncoder = passwordEncoder;
//        this.authenticationManager = authenticationManager;
//        this.jwtService = jwtService;
//    }
//
//    public Users signup(SignUpRequest signUpRequest) {
//        Users users = new Users();
//        users.setId(signUpRequest.getId());
//        users.setEmail(signUpRequest.getEmail());
//        users.setName(signUpRequest.getName());
//        users.setGender(signUpRequest.getGender());
//        users.setTall(signUpRequest.getTall());
//        users.setRole(Role.USER);
//        users.setPw(passwordEncoder.encode(signUpRequest.getPw()));
//
//        return jpaUserRepository.save(users);
//    }
//
//
//    public JwtAuthenticationResponse signin(SignInRequest signInRequest) {
//        authenticationManager.authenticate(
//                new UsernamePasswordAuthenticationToken(signInRequest.getId(), signInRequest.getPw()));
//
//        var users = jpaUserRepository.findById(signInRequest.getId());
//        var jwt = jwtService.generateToken(users);
//
//        JwtAuthenticationResponse jwtAuthenticationResponse = new JwtAuthenticationResponse();
//
//        jwtAuthenticationResponse.setToken(jwt);
//
//        return jwtAuthenticationResponse;
//    }
//}
