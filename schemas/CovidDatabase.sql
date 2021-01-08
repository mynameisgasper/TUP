/*==============================================================*/
/* DBMS name:      PostgreSQL 8                                 */
/* Created on:     08/01/2021 12:15:00                          */
/*==============================================================*/


drop index AGEGROUP_PK;

drop table AGEGROUP;

drop index RELATIONSHIP_18_FK;

drop index APPROVALRATING_PK;

drop table APPROVALRATING;

drop index BYGENDER2_FK;

drop index BYGENDER_FK;

drop index BYGENDER_PK;

drop table BYGENDER;

drop index CITY_PK;

drop table CITY;

drop index CONTINENT_PK;

drop table CONTINENT;

drop index RELATIONSHIP_1_FK;

drop index COUNTRY_PK;

drop table COUNTRY;

drop index RELATIONSHIP_14_FK;

drop index COUNTY_PK;

drop table COUNTY;

drop index RELATIONSHIP_19_FK;

drop index RELATIONSHIP_17_FK;

drop index RELATIONSHIP_15_FK;

drop index RELATIONSHIP_7_FK;

drop index RELATIONSHIP_2_FK;

drop index COVID19_PK;

drop table COVID19;

drop index RELATIONSHIP_16_FK;

drop index RELATIONSHIP_10_FK;

drop index RELATIONSHIP_6_FK;

drop index HOSPITAL_PK;

drop table HOSPITAL;

drop index RELATIONSHIP_21_FK;

drop index MEASURES_PK;

drop table MEASURES;

drop index RELATIONSHIP_9_FK;

drop index SEVERITYPREDICTION_PK;

drop table SEVERITYPREDICTION;

drop index RELATIONSHIP_20_FK;

drop index RELATIONSHIP_5_FK;

drop index STATE_PK;

drop table STATE;

drop index RELATIONSHIP_22_FK;

drop index UNEMPLOYMENT_PK;

drop table UNEMPLOYMENT;

/*==============================================================*/
/* Table: AGEGROUP                                              */
/*==============================================================*/
create table AGEGROUP (
   ID_AGE_GROUP         INT4                 not null,
   AGE_GROUP            VARCHAR(32)          null,
   constraint PK_AGEGROUP primary key (ID_AGE_GROUP)
);

/*==============================================================*/
/* Index: AGEGROUP_PK                                           */
/*==============================================================*/
create unique index AGEGROUP_PK on AGEGROUP (
ID_AGE_GROUP
);

/*==============================================================*/
/* Table: APPROVALRATING                                        */
/*==============================================================*/
create table APPROVALRATING (
   ID_APPROVAL          INT4                 not null,
   ID_RECORD            INT4                 null,
   APPROVAL_ESTIMATE    DECIMAL              null,
   APPROVAL_HIGH        DECIMAL              null,
   APPROVAL_LOW         DECIMAL              null,
   DATE                 DATE                 null,
   constraint PK_APPROVALRATING primary key (ID_APPROVAL)
);

comment on table APPROVALRATING is
'Trump''s approval rating';

/*==============================================================*/
/* Index: APPROVALRATING_PK                                     */
/*==============================================================*/
create unique index APPROVALRATING_PK on APPROVALRATING (
ID_APPROVAL
);

/*==============================================================*/
/* Index: RELATIONSHIP_18_FK                                    */
/*==============================================================*/
create  index RELATIONSHIP_18_FK on APPROVALRATING (
ID_RECORD
);

/*==============================================================*/
/* Table: BYGENDER                                              */
/*==============================================================*/
create table BYGENDER (
   ID_AGE_GROUP         INT4                 not null,
   CODE                 CHAR(2)              not null,
   GENDER               CHAR(1)              null,
   REPORT_DATE          DATE                 null,
   COVID_DEATHS_BY_GENDER INT4                 null,
   TOTAL_DEATHS_BY_GENDER INT4                 null,
   constraint PK_BYGENDER primary key (ID_AGE_GROUP, CODE, GENDER)
);

/*==============================================================*/
/* Index: BYGENDER_PK                                           */
/*==============================================================*/
create unique index BYGENDER_PK on BYGENDER (
ID_AGE_GROUP,
CODE,
GENDER
);

/*==============================================================*/
/* Index: BYGENDER_FK                                           */
/*==============================================================*/
create  index BYGENDER_FK on BYGENDER (
ID_AGE_GROUP
);

/*==============================================================*/
/* Index: BYGENDER2_FK                                          */
/*==============================================================*/
create  index BYGENDER2_FK on BYGENDER (
CODE
);

/*==============================================================*/
/* Table: CITY                                                  */
/*==============================================================*/
create table CITY (
   ID_CITY              INT4                 not null,
   CITY_NAME            VARCHAR(64)          null,
   constraint PK_CITY primary key (ID_CITY)
);

/*==============================================================*/
/* Index: CITY_PK                                               */
/*==============================================================*/
create unique index CITY_PK on CITY (
ID_CITY
);

/*==============================================================*/
/* Table: CONTINENT                                             */
/*==============================================================*/
create table CONTINENT (
   ID_CONTINENT         INT4                 not null,
   CONTINENT_NAME       VARCHAR(16)          null,
   constraint PK_CONTINENT primary key (ID_CONTINENT)
);

/*==============================================================*/
/* Index: CONTINENT_PK                                          */
/*==============================================================*/
create unique index CONTINENT_PK on CONTINENT (
ID_CONTINENT
);

/*==============================================================*/
/* Table: COUNTRY                                               */
/*==============================================================*/
create table COUNTRY (
   ISO                  CHAR(16)             not null,
   ID_CONTINENT         INT4                 not null,
   COUNTRY_NAME         VARCHAR(32)          not null,
   POPULATION           INT4                 null,
   POPULATION_DENSITY   DECIMAL              null,
   MEDIAN_AGE           DECIMAL              null,
   AGED_65_OR_OLDER     DECIMAL              null,
   AGED_70_OR_OLDER     DECIMAL              null,
   GDP_PER_CAPITA       DECIMAL              null,
   EXTREME_POVERTY      DECIMAL              null,
   CARDIO_VASC_DEATH_RATE DECIMAL              null,
   DIABETES_PREVALENCE  DECIMAL              null,
   FEMALE_SMOKERS       DECIMAL              null,
   MALE_SMOKERS         DECIMAL              null,
   HANDWASHING_FACILITIES DECIMAL              null,
   HOSPITAL_BEDS_PER_THOUSAND DECIMAL              null,
   LIFE_EXPECTANCY      DECIMAL              null,
   HUMAN_DEVELOPMENT_INDEX DECIMAL              null,
   constraint PK_COUNTRY primary key (ISO)
);

/*==============================================================*/
/* Index: COUNTRY_PK                                            */
/*==============================================================*/
create unique index COUNTRY_PK on COUNTRY (
ISO
);

/*==============================================================*/
/* Index: RELATIONSHIP_1_FK                                     */
/*==============================================================*/
create  index RELATIONSHIP_1_FK on COUNTRY (
ID_CONTINENT
);

/*==============================================================*/
/* Table: COUNTY                                                */
/*==============================================================*/
create table COUNTY (
   FIPS                 INT4                 not null,
   CODE                 CHAR(2)              null,
   COUNTY_NAME          VARCHAR(64)          not null,
   constraint PK_COUNTY primary key (FIPS)
);

/*==============================================================*/
/* Index: COUNTY_PK                                             */
/*==============================================================*/
create unique index COUNTY_PK on COUNTY (
FIPS
);

/*==============================================================*/
/* Index: RELATIONSHIP_14_FK                                    */
/*==============================================================*/
create  index RELATIONSHIP_14_FK on COUNTY (
CODE
);

/*==============================================================*/
/* Table: COVID19                                               */
/*==============================================================*/
create table COVID19 (
   ID_RECORD            INT4                 not null,
   ID_CITY              INT4                 null,
   CODE                 CHAR(2)              null,
   FIPS                 INT4                 null,
   ISO                  CHAR(16)             not null,
   ID_APPROVAL          INT4                 null,
   REPRODUCTION_RATE    DECIMAL              null,
   NEW_TESTS            INT4                 null,
   NEW_TESTS_PER_THOUSAND DECIMAL              null,
   TOTAL_TESTS          INT4                 null,
   TOTAL_TESTS_PER_THOUSAND DECIMAL              null,
   NEW_TESTS_SMOOTHED   DECIMAL              null,
   NEW_TESTS_SMOOTHED_PER_THOUSAND DECIMAL              null,
   POSITIVE_RATE        DECIMAL              null,
   TESTS_PER_CASE       DECIMAL              null,
   TESTS_UNIT           VARCHAR(128)         null,
   TOTAL_VACCINATIONS   INT4                 null,
   TOTAL_VACCINATIONS_PER_HUNDRED DECIMAL              null,
   STRINGENCY_INDEX     DECIMAL              null,
   NEW_CASES            DECIMAL              null,
   TOTAL_DEATHS__       DECIMAL              null,
   NEW_CASES_SMOOTHED   DECIMAL              null,
   TOTAL_CASES          DECIMAL              null,
   NEW_DEATHS           DECIMAL              null,
   NEW_DEATHS_SMOOTHED  DECIMAL              null,
   ICU_PATIENTS         DECIMAL              null,
   HOSP_PATIENTS        DECIMAL              null,
   WEEKLY_ICU_ADMISSIONS DECIMAL              null,
   WEEKLY_HOSP_ADMISSIONS DECIMAL              null,
   DATE                 DATE                 null,
   constraint PK_COVID19 primary key (ID_RECORD)
);

/*==============================================================*/
/* Index: COVID19_PK                                            */
/*==============================================================*/
create unique index COVID19_PK on COVID19 (
ID_RECORD
);

/*==============================================================*/
/* Index: RELATIONSHIP_2_FK                                     */
/*==============================================================*/
create  index RELATIONSHIP_2_FK on COVID19 (
ISO
);

/*==============================================================*/
/* Index: RELATIONSHIP_7_FK                                     */
/*==============================================================*/
create  index RELATIONSHIP_7_FK on COVID19 (
CODE
);

/*==============================================================*/
/* Index: RELATIONSHIP_15_FK                                    */
/*==============================================================*/
create  index RELATIONSHIP_15_FK on COVID19 (
FIPS
);

/*==============================================================*/
/* Index: RELATIONSHIP_17_FK                                    */
/*==============================================================*/
create  index RELATIONSHIP_17_FK on COVID19 (
ID_CITY
);

/*==============================================================*/
/* Index: RELATIONSHIP_19_FK                                    */
/*==============================================================*/
create  index RELATIONSHIP_19_FK on COVID19 (
ID_APPROVAL
);

/*==============================================================*/
/* Table: HOSPITAL                                              */
/*==============================================================*/
create table HOSPITAL (
   HOSPITAL_ID          INT4                 not null,
   FIPS                 INT4                 null,
   CODE                 CHAR(2)              null,
   ID_SEVERITY          INT4                 null,
   HOSPITAL_NAME        VARCHAR(128)         null,
   TYPE                 VARCHAR(64)          null,
   ADDRESS              VARCHAR(128)         null,
   CITY                 VARCHAR(64)          null,
   ZIP                  VARCHAR(64)          null,
   LICENCED_BEDS        INT4                 null,
   STAFFED_BEDS         INT4                 null,
   ICU_BEDS             INT4                 null,
   ADULT_ICU_BEDS       INT4                 null,
   PEDI_ICU_BEDS        INT4                 null,
   BED_UTILIZATION      DECIMAL              null,
   POTENTIAL            DECIMAL              null,
   AVG_VENTILATION_USE  DECIMAL              null,
   LAT                  DECIMAL              null,
   LON                  DECIMAL              null,
   constraint PK_HOSPITAL primary key (HOSPITAL_ID)
);

/*==============================================================*/
/* Index: HOSPITAL_PK                                           */
/*==============================================================*/
create unique index HOSPITAL_PK on HOSPITAL (
HOSPITAL_ID
);

/*==============================================================*/
/* Index: RELATIONSHIP_6_FK                                     */
/*==============================================================*/
create  index RELATIONSHIP_6_FK on HOSPITAL (
CODE
);

/*==============================================================*/
/* Index: RELATIONSHIP_10_FK                                    */
/*==============================================================*/
create  index RELATIONSHIP_10_FK on HOSPITAL (
ID_SEVERITY
);

/*==============================================================*/
/* Index: RELATIONSHIP_16_FK                                    */
/*==============================================================*/
create  index RELATIONSHIP_16_FK on HOSPITAL (
FIPS
);

/*==============================================================*/
/* Table: MEASURES                                              */
/*==============================================================*/
create table MEASURES (
   MEASURE_ID           INT4                 not null,
   CODE                 CHAR(2)              null,
   INDUSTRY             INT2                 null,
   PERSONAL_CARE        INT2                 null,
   ENTERTAINMENT        INT2                 null,
   OUTDOOR_RECREATION   INT2                 null,
   RETAIL               INT2                 null,
   HOUSE_OF_WORSHIP     INT2                 null,
   FOOD_DRINK           INT2                 null,
   constraint PK_MEASURES primary key (MEASURE_ID)
);

/*==============================================================*/
/* Index: MEASURES_PK                                           */
/*==============================================================*/
create unique index MEASURES_PK on MEASURES (
MEASURE_ID
);

/*==============================================================*/
/* Index: RELATIONSHIP_21_FK                                    */
/*==============================================================*/
create  index RELATIONSHIP_21_FK on MEASURES (
CODE
);

/*==============================================================*/
/* Table: SEVERITYPREDICTION                                    */
/*==============================================================*/
create table SEVERITYPREDICTION (
   ID_SEVERITY          INT4                 not null,
   HOSPITAL_ID          INT4                 not null,
   SEVERITY_1DAY        INT2                 null,
   SEVERITY_2DAY        INT2                 null,
   SEVERITY_3DAY        INT2                 null,
   SEVERITY_4DAY        INT2                 null,
   SEVERITY_5DAY        INT2                 null,
   SEVERITY_6DAY        INT2                 null,
   SEVERITY_7DAY        INT2                 null,
   LAT_HOSPITAL         DECIMAL              null,
   LON_HOSPITAL         DECIMAL              null,
   constraint PK_SEVERITYPREDICTION primary key (ID_SEVERITY)
);

/*==============================================================*/
/* Index: SEVERITYPREDICTION_PK                                 */
/*==============================================================*/
create unique index SEVERITYPREDICTION_PK on SEVERITYPREDICTION (
ID_SEVERITY
);

/*==============================================================*/
/* Index: RELATIONSHIP_9_FK                                     */
/*==============================================================*/
create  index RELATIONSHIP_9_FK on SEVERITYPREDICTION (
HOSPITAL_ID
);

/*==============================================================*/
/* Table: STATE                                                 */
/*==============================================================*/
create table STATE (
   CODE                 CHAR(2)              not null,
   ISO                  CHAR(16)             not null,
   MEASURE_ID           INT4                 null,
   STATE_NAME           VARCHAR(32)          not null,
   POPULATION           INT4                 null,
   COVID_DEATHS         INT4                 null,
   TOTAL_DEATHS         INT4                 null,
   constraint PK_STATE primary key (CODE)
);

/*==============================================================*/
/* Index: STATE_PK                                              */
/*==============================================================*/
create unique index STATE_PK on STATE (
CODE
);

/*==============================================================*/
/* Index: RELATIONSHIP_5_FK                                     */
/*==============================================================*/
create  index RELATIONSHIP_5_FK on STATE (
ISO
);

/*==============================================================*/
/* Index: RELATIONSHIP_20_FK                                    */
/*==============================================================*/
create  index RELATIONSHIP_20_FK on STATE (
MEASURE_ID
);

/*==============================================================*/
/* Table: UNEMPLOYMENT                                          */
/*==============================================================*/
create table UNEMPLOYMENT (
   UNEMPLOYMENT_ID      INT4                 not null,
   ISO                  CHAR(16)             null,
   UNEMPLOYMENT_DATE    DATE                 null,
   VALUE                DECIMAL              null,
   constraint PK_UNEMPLOYMENT primary key (UNEMPLOYMENT_ID)
);

/*==============================================================*/
/* Index: UNEMPLOYMENT_PK                                       */
/*==============================================================*/
create unique index UNEMPLOYMENT_PK on UNEMPLOYMENT (
UNEMPLOYMENT_ID
);

/*==============================================================*/
/* Index: RELATIONSHIP_22_FK                                    */
/*==============================================================*/
create  index RELATIONSHIP_22_FK on UNEMPLOYMENT (
ISO
);

alter table APPROVALRATING
   add constraint FK_APPROVAL_RELATIONS_COVID19 foreign key (ID_RECORD)
      references COVID19 (ID_RECORD)
      on delete restrict on update restrict;

alter table BYGENDER
   add constraint FK_BYGENDER_BYGENDER_AGEGROUP foreign key (ID_AGE_GROUP)
      references AGEGROUP (ID_AGE_GROUP)
      on delete restrict on update restrict;

alter table BYGENDER
   add constraint FK_BYGENDER_BYGENDER2_STATE foreign key (CODE)
      references STATE (CODE)
      on delete restrict on update restrict;

alter table COUNTRY
   add constraint FK_COUNTRY_RELATIONS_CONTINEN foreign key (ID_CONTINENT)
      references CONTINENT (ID_CONTINENT)
      on delete restrict on update restrict;

alter table COUNTY
   add constraint FK_COUNTY_RELATIONS_STATE foreign key (CODE)
      references STATE (CODE)
      on delete restrict on update restrict;

alter table COVID19
   add constraint FK_COVID19_RELATIONS_COUNTY foreign key (FIPS)
      references COUNTY (FIPS)
      on delete restrict on update restrict;

alter table COVID19
   add constraint FK_COVID19_RELATIONS_CITY foreign key (ID_CITY)
      references CITY (ID_CITY)
      on delete restrict on update restrict;

alter table COVID19
   add constraint FK_COVID19_RELATIONS_APPROVAL foreign key (ID_APPROVAL)
      references APPROVALRATING (ID_APPROVAL)
      on delete restrict on update restrict;

alter table COVID19
   add constraint FK_COVID19_RELATIONS_COUNTRY foreign key (ISO)
      references COUNTRY (ISO)
      on delete restrict on update restrict;

alter table COVID19
   add constraint FK_COVID19_RELATIONS_STATE foreign key (CODE)
      references STATE (CODE)
      on delete restrict on update restrict;

alter table HOSPITAL
   add constraint FK_HOSPITAL_RELATIONS_SEVERITY foreign key (ID_SEVERITY)
      references SEVERITYPREDICTION (ID_SEVERITY)
      on delete restrict on update restrict;

alter table HOSPITAL
   add constraint FK_HOSPITAL_RELATIONS_COUNTY foreign key (FIPS)
      references COUNTY (FIPS)
      on delete restrict on update restrict;

alter table HOSPITAL
   add constraint FK_HOSPITAL_RELATIONS_STATE foreign key (CODE)
      references STATE (CODE)
      on delete restrict on update restrict;

alter table MEASURES
   add constraint FK_MEASURES_RELATIONS_STATE foreign key (CODE)
      references STATE (CODE)
      on delete restrict on update restrict;

alter table SEVERITYPREDICTION
   add constraint FK_SEVERITY_RELATIONS_HOSPITAL foreign key (HOSPITAL_ID)
      references HOSPITAL (HOSPITAL_ID)
      on delete restrict on update restrict;

alter table STATE
   add constraint FK_STATE_RELATIONS_MEASURES foreign key (MEASURE_ID)
      references MEASURES (MEASURE_ID)
      on delete restrict on update restrict;

alter table STATE
   add constraint FK_STATE_RELATIONS_COUNTRY foreign key (ISO)
      references COUNTRY (ISO)
      on delete restrict on update restrict;

alter table UNEMPLOYMENT
   add constraint FK_UNEMPLOY_RELATIONS_COUNTRY foreign key (ISO)
      references COUNTRY (ISO)
      on delete restrict on update restrict;

