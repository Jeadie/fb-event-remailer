

# Components
 ## Webhooks

  ### Setup Webhook for User
  * Can create Webhooks programmatically via App subscriptions: 
    Example: (https://stackoverflow.com/questions/55429169/how-to-programmatically-subscribe-messenger-webhook)
    ```
     curl -F "object=user" \
          -F "callback_url=https://your-clever-domain-name.com/webhooks" \
          -F "fields=photos" \
          -F "verify_token=your-verify-token" \
          -F "access_token=your-app-access-token" \
          "https://graph.facebook.com/your-app-id/subscriptions"
    ```
  
  ### Process Webhook events
   * Parse details of event from event id, etc
   * Construct email and send
   

  ### HTTPS infrastructure
   * Using AWS:
     * API Gateway
      * Handle HTTPS confirmation on Webhooks
      * Handle incoming webhook requests


 ## UI for account setup
 
  ### Grant App permissions for user's events, etc.

  ### Persistent store for user's ids, emails etc.
