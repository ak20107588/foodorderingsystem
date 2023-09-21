#Project:- Food Ordering System

In this project we use MySQL for Database and we also use all images in this
project from online link.

we create db with name BurgerPoint and also add database details in django project settings page.
We also add databse model all details in django project app model.


Query:

create database BurgerPoint;
use BurgerPoint;

and now we add all details of product images,price,name of product.

Query:

insert into app1_product values(1,'McAloo Tikki','https://5.imimg.com/data5/SH/WO/MY-24590086/aloo-tikki-burger-500x500.jpg',55,false,50),
(2,'McVeggie','https://www.pngfind.com/pngs/b/164-1642134_veggie-burger-mcdonalds-mcveggie-hd-png-download.png',120,true,110),
(3,'McPaneer','https://lh3.googleusercontent.com/9iMbJAXYWonxnh1TyKdAgtsQAnH6kqWbHxjFqQjD5sdyF4DbI-dybFqwl2kzGMTZZOA0J8c2oFvkwHvHSXKwOoiazGqTNsFv6_oOLMm2',150,false,140),
(4,'McChicken','https://alchetron.com/cdn/mcchicken-e5dc26b9-c3d5-4a0e-bec7-0601a995d78-resize-750.png',140,true,130),
(5,'McSpicy Chicken','https://goodyfeed.com/wp-content/uploads/2020/10/mcspicy.png',180,false,170),
(6,'McAmerican Veg','https://lh3.googleusercontent.com/Uo7zY2TRhEc9MQH8gln8Sd0461XWqoICCd9M8XDBlhL1rYWlKCfuL5Puyw3VYDaIFpvxOpw0xhi1QaPadstp8RC3flRoGSz7OSLiBMeSWg=w512-rw',130,false,120),
(7,'McEgg','https://i.pinimg.com/originals/ec/93/18/ec93185334de6ad8898ebe336ba23ab6.png',60,false,55),
(8,'McFilet O Fish','https://content.wkyc.com/photo/2016/02/26/Filet-O-Fish_1456496078194_436797_ver1.0.jpg',160,true,150),
(9,'McVeg Maharaja','https://qph.cf2.quoracdn.net/main-qimg-2e658896477d3ecfdd311e2b298e2b25',200,true,190),
(10,'McChicken Nuggets(9pcs)','https://vehicleforest.com/blog/wp-content/uploads/2023/04/McDonalds-tasty-nuggets-Price-in-india.png',220,false,200),
(11,'McFrench Fries','https://mcdonalds.com.lb/storage/menu-categories/Sides.png',120,true,110),
(12,'McFlurry Oreo','https://lh3.googleusercontent.com/qI0RWse4wH5svGRv5Vc63uXai_JWXvZWHn8BXRXPTnKZjsIeKtOFzePUhkA6zX8QhaD_pMsCJyzDJ6BQlT6I6X9NNjTfpA6Y1It8sNQI',95,true,85),
(13,'McStrawberry SoftServe','https://mcdonalds.com.au/sites/mcdonalds.com.au/files/YMAL_Desserts_StrawberrySundae.png',95,false,85),
(14,'McBrownie SoftServe','https://live.staticflickr.com/1580/25083009612_293a9656e3.jpg',130,true,115);