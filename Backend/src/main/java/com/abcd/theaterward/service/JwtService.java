//package com.abcd.theaterward.service;
//
//import com.abcd.theaterward.domain.Users;
//import io.jsonwebtoken.Claims;
//import io.jsonwebtoken.Jwts;
//import io.jsonwebtoken.SignatureAlgorithm;
//import io.jsonwebtoken.io.Decoders;
//import io.jsonwebtoken.security.Keys;
//import org.springframework.security.core.userdetails.UserDetails;
//import org.springframework.stereotype.Service;
//
//import java.security.Key;
//import java.util.Date;
//import java.util.function.Function;
//
//@Service
//public class JwtService {
//    public String generateToken(Users users) {
//        return Jwts.builder().setSubject(users.getId())
//                .setIssuedAt(new Date(System.currentTimeMillis()))
//                .setExpiration(new Date(System.currentTimeMillis() + 1000 * 40 * 24))
//                .signWith(getSignKey(), SignatureAlgorithm.HS256)
//                .compact();
//    }
//
//    private <T> T extractClaim(String token, Function<Claims, T> claimsResolvers) {
//        final Claims claims = extractAllClaims(token);
//        return claimsResolvers.apply(claims);
//    }
//
//    private Claims extractAllClaims(String token) {
//        return Jwts.parserBuilder().setSigningKey(getSignKey()).build().parseClaimsJws(token).getBody();
//    }
//
//    public String extractUserName(String token) {
//        return extractClaim(token, Claims::getSubject);
//    }
//
//
//    private Key getSignKey() {
//        byte[] key = Decoders.BASE64.decode("413F4428f72BfB6250655368566D5970337336763979244226452948404D6351");
//        return Keys.hmacShaKeyFor(key);
//    }
//
//    public boolean isTokenValid(String token, UserDetails userDetails) {
//        final String userid = extractUserName(token);
//        return (userid.equals(userDetails.getUsername()) && !isTokenExpired(token));
//    }
//
//    private boolean isTokenExpired(String token) {
//        return extractClaim(token, Claims::getExpiration).before(new Date());
//    }
//}
