We're getting pretty close to the end of the project, so how about a quick summary of our <del>neutralizing</del> gaming strategy?

As you may have seen on some photographs of our robot, we have **one big rotating arm** in the middle and two smaller ones on each front side in order to grab the balls.
Apart from the tracks, we add on top of that **a bunch of sensors** whose roles are to help the robot navigate on the field:

<ul>
<li>a <i>color sensor</i>, to detect when we have caught a blue or red ball. In that case we want the robot to stop moving the arm, finish his turn and go to the net in order to throw the ball over.</li>

<li>a <i>touch sensor</i>, to detect when we hit a wall.</li>

<li>an <i>ultrasonic sensor</i>, to detect the net since we are not supposed to touch it (as it is the case for the walls) unless we want to lose points.</li>

<li>a <i>light sensor</i>, to be sure we follow correctly the net without running into it.</li>
</ul>

Equipped with that arsenal, we need an effective and not too complex **strategy**. Here is what we agreed on:
The robot starts on his landing area and performs some patrols around the field. When a ball is caught, we finish our round in order to face the net, stop and <del>FIRE!</del> throw the ball over. And whatnot...
However, problems may occur when we haven't found any ball for a while. In that case, we change the radius of effect and perform smaller or wider squares to be sure we take a bite out of something!

What is funny and interesting about our strategy is that unlike many other groups, we are basically not looking for any ball. We merely rely on the fact that the patrol leads to having some balls caught by the rotating arm, which eventually makes our coding easier.


