#!/bin/bash
# makes a request to the serve to respond with a message You got me!
curl -o /dev/null -sw "You got me!" 0.0.0.0:5000/catch_me
