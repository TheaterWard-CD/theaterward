package com.abcd.theaterward.domain;


import jakarta.persistence.*;

@Entity
@Table(name = "theater")
public class Theater {
    @Id
    @Column(name = "theater_no")
    private int theaterNo;

    @Column(name = "theater_name")
    private String theaterName;

    @Column(name = "theater_wall", columnDefinition = "JSON")
    private String theaterWall;

    @Column(name = "theater_obj", columnDefinition = "JSON")
    private String theaterObj;

    @Column(name = "theater_stage", columnDefinition = "JSON")
    private String theaterStage;

    @Column(name = "gltf", columnDefinition = "LONGTEXT")
    private String gltf;

    public String getTheaterStage() {
        return theaterStage;
    }

    public void setTheaterStage(String theatersStage) {
        this.theaterStage = theatersStage;
    }

    public String getTheaterObj() {
        return theaterObj;
    }

    public void setTheaterObj(String theatersObj) {
        this.theaterObj = theatersObj;
    }

    public String getTheaterWall() {
        return theaterWall;
    }

    public void setTheaterWall(String theatersWall) {
        this.theaterWall = theatersWall;
    }

    public String getTheaterName() {
        return theaterName;
    }

    public void setTheaterName(String theaterName) {
        this.theaterName = theaterName;
    }

    public int getTheaterNo() {
        return theaterNo;
    }

    public void setTheaterNo(int theaterNo) {
        this.theaterNo = theaterNo;
    }

    public String getGltf() {
        return gltf;
    }

    public void setGltf(String gltf) {
        this.gltf = gltf;
    }
}
