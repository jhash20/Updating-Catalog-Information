# Updating-Catalog-Information

Description:

Scripts to upload new products (images and descriptions) to an online store using two different web endpoints and send a report to the supplier, notifying them about what was imported. Also includes a script to run on the web server to monitor its health and send an alert if there is a web server health concern.


Project Problem Statement:

You work for an online fruit store, and you need to develop a system that will update the catalog information with data provided by your suppliers. When each supplier has new products for your store, they give you an image and a description of each product.

Given a bunch of images and descriptions of each of the new products, you’ll:
  1. Upload the new products to your online store. Images and descriptions should be uploaded separately, using two different web endpoints.
  2. Send a report back to the supplier, letting them know what you imported.
Since this process is key to your business's success, you need to make sure that it keeps running! So, you’ll also:
  1. Run a script on your web server to monitor system health.
  2. Send an email with an alert if the server is ever unhealthy.
