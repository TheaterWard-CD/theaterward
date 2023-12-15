package com.abcd.theaterward.domain;

import java.util.HashMap;
import java.util.Map;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonMappingException;
import com.fasterxml.jackson.databind.ObjectMapper;


public class TheaterP {


    private int theaterNo;
    private String theaterName;
    private String theaterWall;
    private String theaterObj;
    private String theaterStage;
    private Map<String, Object> gltf = new HashMap<>();

    public TheaterP(Theater t) {
        this.theaterNo = t.getTheaterNo();
        this.theaterName = t.getTheaterName();
        this.theaterWall = t.getTheaterWall();
        this.theaterObj = t.getTheaterObj();
        this.theaterStage = t.getTheaterStage();
        try {
            ObjectMapper objectMapper = new ObjectMapper();
            this.gltf.put("gltf", objectMapper.readValue(t.getGltf(), Object.class));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public int getTheaterNo() {
        return theaterNo;
    }

    public void setTheaterNo(int theaterNo) {
        this.theaterNo = theaterNo;
    }

    public String getTheaterName() {
        return theaterName;
    }

    public void setTheaterName(String theaterName) {
        this.theaterName = theaterName;
    }

    public String getTheaterWall() {
        return theaterWall;
    }

    public void setTheaterWall(String theaterWall) {
        this.theaterWall = theaterWall;
    }

    public String getTheaterObj() {
        return theaterObj;
    }

    public void setTheaterObj(String theaterObj) {
        this.theaterObj = theaterObj;
    }

    public String getTheaterStage() {
        return theaterStage;
    }

    public void setTheaterStage(String theaterStage) {
        this.theaterStage = theaterStage;
    }

    public Map<String, Object> getGltf() {
        return gltf;
    }

    public void setGltf(Map<String, Object> gltf) {
        this.gltf = gltf;
    }
}
