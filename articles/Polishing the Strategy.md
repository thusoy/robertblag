More secret details on our winning strategy for next week's competition.

In the [previous article](http://bob.thusoy.com/robot-badass-strategy.html) we saw our basic strategy, which hasn't changed a lot throughout the project. Until recently!

Over the last few days, we tried to optimize the code and changed some aspects in Robert's behaviour:

* We now start with full magazine (one ball already on the arm), start our patrol and immediately throw this ball when we reach the net.

* Some balls are placed close to the net and thanks to our routine having been optimized, those balls are caught and thrown quickly afterwards. 
This is a pretty huge improvement because the robot used to finish his turn (~19s) before throwing this ball over the net. 

* We plan to optimize also the turning detection, which you will get more information about in a new article.


Basically, our program runs thanks to three main tasks:

* *collect*, which uses the color sensor and keeps making the arm rotate until we catch a red or a blue ball (which sets the flag ballLoaded).

* *trace*, which prevents our robot from running into the net in case we have performed a bad turn. If it's the case, the robot stops and changes direction to go away from the net.

* our *main*, which in essence starts with a setup of the unmetioned sensors and applies the strategy we've talked about, making calls to collect and trace at the right time.
We also use a Bluetooth connection with the NXT in order to get directly information about the robot on a computer. We already showed the code for the server [here](http://bob.thusoy.com/anal-expulsiveness.html) and also added two files for our robot, btio and btlog, that wait for a connection and enable the robot to send messages.

