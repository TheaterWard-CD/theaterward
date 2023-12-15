package com.abcd.theaterward.domain;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

import java.util.Collection;
import java.util.List;

@Entity
@Table(name = "users")
public class Users {
    @Id
    @Column(name = "users_id")
    private String id;

    @Column(name = "users_pw")
    private String pw;

    @Column(name = "users_name")
    private String name;

    @Column(name = "users_email")
    private String email;

    @Column(name = "users_gender")
    private String gender;

    @Column(name = "users_tall")
    private int tall;

    @Column(name = "role")
    private Role role;

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getPw() {
        return pw;
    }

    public void setPw(String pw) {
        this.pw = pw;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }

    public int getTall() {
        return tall;
    }

    public void setTall(int tall) {
        this.tall = tall;
    }

    public Role getRole() {
        return role;
    }

    public void setRole(Role role) {
        this.role = role;
    }


}
