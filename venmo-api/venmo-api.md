#venmo developer api

###**using venmo to make your apps even better**

^special thanks to Cassidy Williams for helping me with this! You're great.
For those listening, if you don't understand, don't stress. It's going to be okay. I don't always understand everything. Ask questions!

---

using the developer api is super easy :smile: :+1:

---

there are **two main** ways to use the api:

1. payment links

2. REST api/OAuth

---

there is a third way, that i'll touch on quickly...

**Drop ins for iOS and Android**

---

![fit](imgs/venmo_ios_sdk.gif)

---

#### 1. Create your app on Venmo

#### 2. Configure your Xcode project

#### 3. Initialize the Venmo iOS SDK

#### 4. Choose a transaction method

#### 5. Request permissions

#### 6. Send a payment

^We recommend using CocoaPads for iOS
Moving away from focusing on "drop ins" aka the iOS and android SDKs (for now)

---

*android is just as easy*

for more info... <br>

https://github.com/venmo/venmo-ios-sdk/ <Br>

https://github.com/venmo/app-switch-android

---

but back to the two main ways!

let's talk about the first:<br>

#**payment links**

---

![fit](imgs/paymentlinks.png)

  ---

  **so simple it's almost absurd**

  ---

  let's talk about the second: <br>

#**REST api/OAuth**

  ---

#**THE RULE**

  in order to use the REST api with venmo, you must be implementing OAuth

  BUT! you don't necessarily have to implement OAuth using the REST api

  ---

  i know, i know. **squares** and **rectangles**

  ---

![fit]()


  ^something example from this: https://developer.venmo.com/docs/authentication

  ----

  so fun! amirite! :dancer:

  ---

  we also have a **sandbox** for you to use when testing payments so you don't go broke. that said, if for whatever reason you'd like to practice sending payments to **me** by all means be my guest!

  ---

(and as another side note)

  you can make use cURL requests to make payments with the api

  ```curl --data "access_token=INSERTHERE&user_id= INSERTHERE&note=AWESOME%20DEMO%TERRI&amount=0.01" https://api.venmo.com/v1/payments```

  ^not most recommended way to use the api, but mentioning just in case

  ---

  all of this and more can be found at <br>

#**developer.venmo.com**

  ---

  for more resources like code samples, tutorials, and working examples, visit <Br>

#**github.com/venmo**

  ---

  :sunny::100::bread:

  **terri@venmo.com** / **@tcburning**

  ---

  you are all :star:s. good luck!


