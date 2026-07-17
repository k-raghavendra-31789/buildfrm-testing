# Databricks notebook source
# COMMAND ----------
%sql
CREATE CATALOG IF NOT EXISTS traffic_lakehouse;
CREATE SCHEMA IF NOT EXISTS traffic_lakehouse.bronze;
CREATE SCHEMA IF NOT EXISTS traffic_lakehouse.silver;

SHOW CATALOGS LIKE 'traffic_lakehouse';
SHOW SCHEMAS IN traffic_lakehouse;
