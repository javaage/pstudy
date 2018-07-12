/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     7/12/2018 5:36:51 PM                         */
/*==============================================================*/


drop table if exists TSHR_AGGR;

/*==============================================================*/
/* Table: TSHR_AGGR                                             */
/*==============================================================*/
create table TSHR_AGGR
(
   AGGR_DATE            date not null,
   AGGR_CODE            varchar(6) not null,
   AGGR_HIGH            int not null,
   AGGR_LOW             int not null,
   unique key AK_KEY_1 (AGGR_DATE, AGGR_CODE)
);

