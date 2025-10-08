#A list of hiccups for our next time around.

1. Signal Acquisition & Hardware Setup
* Issue: Getting the EEG hardware (Unicorn headset) to properly connect and maintain stable data acquisition took over 2 hours. The headset frequently stopped streaming data mid-session, forcing restarts.
* Lesson: Always test hardware ahead of time if possible and prepare fallback workflows (e.g., simulated EEG data streams). Keep electrode gel and cleaning supplies handy, and assign one teammate solely to monitor signal stability.

2. Classifier Training & P300 Paradigm Design
* Issue: The initial classifier performance was poor. We discovered that our early P300 setup lacked proper non-target flashes, ISI tuning, and appropriate stimulus presentation timing.
* Fix: We consulted research papers and adjusted parameters
ISI ≈ 0.75 s, stimulus duration ≈ 0.2 s
All non-target stimuli flash to serve as baseline (P300b)
Switched from RCP to single-stimulus flickering paradigm
Increased trial count for stronger classifier reliability
* Lesson: The classifier needs clear contrast between target and non-target trials. Even “non-interesting” flashes are critical for building a stable baseline.

3. Data Transmission & Networking
* Issue: The Unicorn Suite’s P300 speller sent overly complex UDP packets containing binary image bytes instead of simple classification tags (e.g., “Left,” “Right,” “Up,” “Down”). This caused major parsing and lag issues.
* Fix: We wrote a custom Python parser using regular expressions to extract only the relevant classification outputs.
* Lesson: Always inspect the data stream format early on — understand exactly what’s being sent, and simplify the communication pipeline before integrating it into gameplay logic.

4. Interfacing with the Game (PyGame)
* Issue: Sending classifier output to the maze game was difficult. The LSL pipeline didn’t work as intended, and UDP-based communication introduced delay and occasional desynchronization.
* Fix: Implemented a simplified UDP bridge script to handle message passing between the Unicorn Suite and Python game.
* Lesson: In hackathon settings, prioritize simplicity over elegance. A direct UDP/JSON approach can often outperform LSL if documentation or device compatibility is lacking.

5. Software Limitations & Suite Confusion
* Issue: We initially used the Unicorn Speller suite and built our own game interface from scratch — later realizing Unicorn already had a Platformer and Game Suite that could’ve served as a perfect starting point.
* Lesson: Don’t reinvent the wheel. Always explore built-in software features before developing your own pipeline. Reading through the manufacturer’s demo documentation (even briefly) can save hours.

6. Technical Bottlenecks
* Issue: 
- Only one PC available, limiting parallel development. 
- Dual-monitor setup introduced graphical lag.
- PNG files caused unexpected compatibility issues in the Unity/PyGame environment.
* Lesson: Always test visual assets and network connections on the actual setup you’ll be using. Offload tasks like presentation prep, documentation, or result visualization to remote teammates to maximize in-person efficiency.

7. Team Dynamics & Project Scope
* Observation: The team had varied experience levels — some strong coders, others new to EEG. Despite shortcuts via the Unicorn Suite and open-source game assets, integrating everything still demanded constant debugging and adaptation.
* Lesson: Pre-hackathon alignment on roles, expectations, and technical familiarity saves friction. “Using existing tools effectively” is not laziness — it’s smart engineering. The real work is in integration and problem-solving under pressure.

9. Delaying on the presentation and visuals front
* Not taking enough pictures or videos (not even screenshots or recordings) left us with minimal content for the presentation.
* Not having started the presentation slides until after the lab was closed made up work over-time/late resulting in less-than-ideal quality exposition. 
* Lesson: Assign a person to conduct media collection and start designing the presentation side of things, its probably the most overlooked yet essential part - Being able to sell your idea is what brings it value in people’s eyes. 

## Key Takeaways
* Learn your hardware/software stack thoroughly before designing experiments.
* Debug the communication layer first — it’s usually the bottleneck.
* Hackathons reward adaptability, not perfection.
* EEG setups are inherently finicky — patience and signal monitoring matter more than fancy ML.
* Teaching teammates new to EEG during setup was slow but rewarding; good documentation (like this!) will help future collaborations.