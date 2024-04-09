# [By Noveline ](https://by-noveline-a60b58beb7bd.herokuapp.com/)

![by noveline mockup](docs/readme-img/bn-mockup.png)

## Table of Contents

- [By Noveline](#by-noveline)
- [UX](#ux)
- [Agile Methodology](#agile-methodology)
- [Entity-Relationship Diagram](#entity-relationship-diagram)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Future Features](#future-features)
- [Design](#design)
  - [Logotype](#logotype)
    - [Favicon](#favicon)
  - [Color Scheme](#color-scheme)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
  - [Responsiveness & Performance](#responsive-&-performance)
    - [Lighthouse Testing](#lighthouse-testing)
  - [Code Validation](#code-validation)
  - [Feature Testing](#feature-testing)
- [Deployment](#deployment) 
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

***

### By Noveline

This e-commerce website was built on the request of a family owned business that wanted to expand their target market. Their customers was before obligated to visit a pysical store to explore the products and By Novelines market was limited. By building them a userfriendly and elegant webshop could By Novelines market expand World Wide.

BY Noveline offers elegant and luxury engagement, and weddingrings that is made on request from the customer.

*By Noveline is a fictive business*

### UX

The goal for the e-commerce website By Noveline is to create a user-friendly and secure application where customers can browse products, save them to their shopping cart and then purchase them with full security through Stripe Payments.

### Agile Methodology

Agile was used for efficient planning and development of the website, ensuring alignment with UX requirements.

11 Milestones with related EPIC's divided into UserStorys, UserStory-Admin and Development was setup and followed to fullfil the development of the project By Noveline.

Full project planning can be found here:
[Project Kanban Board for By Noveline](https://github.com/users/SaraTisell/projects/6)

### Entity-Relationship Diagram

<details>
<summary>ERD Planning stage</summary>
<img src="docs/readme-img/bn-erd-planning.png">
</details>


### Features

#### Existing Features

##### Navigation

Navigation meanu is visible for all users and placed in the header.
* Logotype
  * Navigates a user back to home page
* Product nav
  * Takes a user to the desired product page
    * All products
    * Gold Rings
    * Silver Rings
    * Ring Sets
* Profile
  * Regular User
    * SignUp
    * Login
  * User with account 
    * My Profile
      * Order History
      * Personal Info
      * Wishlist
      * Logout
  * Admin user 
    * Orders
    * Product Management
    * Inbox
    * Logout
* Shopping Cart
  * Checkout

###### Footer Navigation

* Customer Service
  * Contact us
  * Privacy Policy

#### Home Page 

The homepage display insperation image with link to product page.

#### Account

A user has the possibility to create an account to save and store their personal information, see order history and save products to their wishlist.

#### Shopping Cart

A user, with or without an account is able to add/remove products from their shoppingcart. If the user want to purchase, they can easy go to shopping cart and navigate to secure checkout. 

#### Checkout 

A user is able to fill in valid information and purchase products at the ceckout page. If the user has an account, they are able to save the information to their profile.

#### My Profile

A user has their own profile page where they can see their order history, personal information and wishlist.
#### Wishlist

A user with an account can save products to their wishlist and display these later isnide their own profile page.

#### Admin Features

Admin has their own profile navigation including:
* Orders
  * All orders is displayed at this page with information regarding the order
* Product Management
  * Add product
  * Edit product
  * Delete product
* Inbox
  * Messages sent through the contact form is displayed at inbox page

#### Contact

A user is able to send in a contact form if they desire to get in touch with the team at By Noveline.

#### Product Pages

Four different pages is displayed at the header menu

* All products
  * Includes all product avaiable in the store
* Gold Rings
  * All product in the category gold rings
* Silver Rings
  * All products in the category silver rings
* Ring Sets
  * All products in the category ring sets

#### Search Function

The user is able to search for specific products through the search form.