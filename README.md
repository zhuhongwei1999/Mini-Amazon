# Mini-Amazon Full Stack Web Application

### Intro

Mini-Amazon is a full-stack web application that simulates an Amazon-like e-commerce system, complete with a fully functioning warehouse and delivery system. The application's frontend is built with Django, while the backend is developed in Python. User data is saved and organized in Postgres and Google Protocol Buffer is used for communication with the world-simulator and mini-UPS system partner.

### Usage

1. Open world simulator

   ```bash
   cd world_simulator_exec/docker_deploy
   sudo docker-compose up
   ```

2. Change the World and UPS hostname and port number in `MiniAmazon/backend/amazon_server.py`

3. Run the Mini-Amazon Web

   ```bash
   cd MiniAmazon
   sudo docker-compose up
   ```

### Business Logic

This project works in coordination with Mini-UPS, which follows the same communication protocol. The business logic for this project is as follows:

1. The user places an order for a product on Amazon.
2. Amazon saves the order information in the database and retrieves the item from the warehouse stock.
3. The warehouse packages the item, and Amazon passes the message to Mini-UPS.
4. Mini-UPS dispatches the appropriate truck from the truck warehouse and arrives at the corresponding warehouse.
5. The warehouse loads the item onto the truck, and based on the order information, it is delivered to the location specified by the customer.

### Feature List

Basic Features

1. **Product Purchasing:** Users can buy a wide range of products, with seamless integration between Mini-Amazon, the world simulator, and UPS.
2. **Catalog Diversity:** Multiple product categories to choose from.
3. **Order Status:** Users can easily check the status of their orders.
4. **Delivery Address Specification:** Users can set their preferred delivery location.
5. **UPS Account Integration:** Orders can be associated with a specific UPS account.

Additional Features:

1. **Trending Items Homepage:** Offers users a curated selection of popular items for a more personalized shopping experience.
2. **Advanced Search Bar:** Allows product searches by name, category, or price range. Users can sort results by price and sales.
3. **Enhanced Shopping Cart:** Lets users add products, view cart contents, modify item quantities, or remove items. It updates the total price dynamically based on the changes made.
4. **Star Rating System:** Customers can rate their purchased products on a scale of 1 to 5 stars. These ratings are displayed on product pages.
5. **Reward Points System:** Encourages purchasing by offering customers 1% credit back on all purchases, displayed on their profile page.
6. **Email Notifications:** Confirmation emails are sent to users at different stages of the order process - placement, shipment, and delivery.
7. **User Profile Customization:** Allows users to view and modify their profile information including email address, bank account, UPS account, delivery address, and a personalized avatar.

### Demo

<img src="https://s1.ax1x.com/2023/07/02/pCDeBvT.png" alt="1" style="zoom:67%;" />

<img src="https://s1.ax1x.com/2023/07/02/pCDerKU.png" alt="1" style="zoom:80%;" />

<img src="https://s1.ax1x.com/2023/07/02/pCDesrF.png" alt="1" style="zoom:80%;" />

<img src="https://s1.ax1x.com/2023/07/02/pCDeyb4.png" alt="1" style="zoom:80%;" />