# Psycho-Acoustic Temperament Hierarchy (PATH)

## Summary

PATH is a tuning theory and method for pianos and other fixed keyboard instruments with natural variations in inharmonicity. It can be used for any keyboard instrument with a fixed pitch, even with no inharmonicity. It is easy enough for instrumentalists to implement, test, and therefore maintain, due to its design leveraging scientific reproducibility.

It is based on new tuning and contrapuntal theories, also presented, providing a new foundation for future tuning and orchestration techniques. 

A theory is presented describing the mathematic and scientific effects of tuning for psychoacoustic consonance, and a technique is developed from the theory. Instead of focusing on mitigations, the focus is on consonance.

The theory describes an inharmonicity coefficient that stretches octaves across the pythagorean comma, and the resulting psychoacoustic properties that vary across arbitrary inharmonicity coefficients in between that wide value and 0. The technique is developed as a recursive-descent optimization algorithm that solves for contrapuntal consonance and "shaped" dissonance under the theory, noting that consonance can be held fixed for entire classes of intervals relating to counterpoint intervals. 

No beat counting is used. Only consonant-sounding 8ths and 5ths are used, tuning most 8ths, 5ths, and 4ths with deliberate psychoacoustic properties, while letting the logarithmic inharmonicity of the instrument evenly distribute the remaining intervals. A self-similar, hierarchical temperament pattern evenly distributes the contrapuntal psychoacoustic consonant properties, rather than focusing on evenly controlling the irrationalities in a single, small temperament range.

## Synopsis

It will be shown mathematically that a higher level of inharmonicity is closer to ideal, and it is easier to tune by ear through metrics of consonance rather than through beat counting. 

It will be shown that the preference for beat counting has design problems, both aesthetic and scientific.
- The aesthetic issue is that psychoacoustic *effects* should have priority, therefore psychoacoustic *methods* should have priority, whether biological methods or modeled methods. Therefore, beat-counting, whether for the initial tuning, or a check tuning, is discouraged as non-psychoacoustic.
- The scientific issues are that beat counting has convergence problems that lower reproducibility, and using subjective master tunings is inherently not reproducible, or only reproducible on the reference, test piano. That problem creates a bias toward master-apprentice relationships in the field, rather than developing as an open, scientific field, accessible to any player of the instrument. The apprenticeship aspect should be left to piano technician activities, but tuning should be available to any instrumentalist.

It will be shown that the psychoacoustic definition of counterpoint suits a particular design for its tuning system. 

## Background

The typical method for tuning a piano is based on a 12 note reference temperament of a single octave to be extrapolated across the remaining octaves. This is a general tuning method that makes sense when thinking in terms of interval ratios first, as expected when tuning is presented only as a mathematical problem. It is optimal for instruments of low inharmonicity, and low amounts of change in inharmonicity across pitch, like the middle of a Steinway. However, most pianos are not Steinways, most pianos have arbitrary levels of inharmonicity, and most concert music spans many octaves. 

Smaller ratios are now favored when piano tuning by ear because the beats can more easily be "felt", because the beats are faster. That is, the tuning errors are more significant as beats when tuning smaller intervals, so it is easier to mitigate beat errors of the smaller intervals. However, faster beats are also harder to converge on.

Beat counting itself has theoretical flaws which defy the common sense notion that consonance is much easier felt than the specifics of a dissonance. It is possible to reformulate tuning as a distribution of consonance with known dissonant effects, allowing any ear to keep a piano tuning maintained with nominal musical training. 

### Counterpoint as a Theory of Consonance, not Dissonance

Even counterpoint only concerns itself with the property of consonance, discarding any consideration for classes of dissonance. It is, after all, the masking effect of consonance that counterpoint addresses. The first actual compositional problem in music was not dissonance, but the interference that harmonic consonance had on polyphonic melodic lines. Instead of trying to control dissonance, counterpoint controls consonance.

This may be unintuitive for an instrumentalist struggling to maintain the pitch of the instrument, but for a composer it is the unexpected harmonic alignments that interfere with the control of melodic lines. Counterpoint allows the composer to move compounded melodic lines across consonance in expected, controlled patterns that become useful compositional devices. The instrumentalist is focusing intervals on controlled pitch, while the composer is focusing intervals on producing controlled harmonic patterns. The composer is rarely bothered about a particular pitch, but an instrumentalist might be obsessed. The different tasks have very different mindsets of approach. 

### Tuning Inharmonic Instruments by Ear has Irrationality

During the development of counterpoint in the Baroque period, tuning systems were theoretically designed around rational intervals, but tunings could only be implemented by ear, so tunings could only be implemented along psychoacoustic alignments which aren't truly rational. Even though ratios were prescribed, measurement was done by ear, so the inharmonicity of octaves, and the lack of understanding of inharmonicity, limited tuning system design to a single octave of 5ths, because octaves could not reproduce the effects of the ratios. That prevented the formal distribution of the pythagorean comma across multiple octaves by ear, which is now possible.

At that time, tuning beats wide to spread the Pythagorean comma was understood, but there was considerable debate, one side arguing to spread the Pythagorean comma completely evenly, the other side arguing to leave select intervals beatless. The argument to spread evenly is to have effects be reproducible across key changes, but it is actually easier to converge on a tuning when fewer intervals are to be tempered.

On the side of even temperament, the *composer* is asking for reproducibility, and on the side of consonant temperament, the *tuner* is asking for reproducibility. The debate effectively ends with the tuner giving up attempting to converge on an optimal tuning, the composer expecting convergence, and the instrumentalist working with whatever has converged. But there should be no reason why both cannot demand reproducibility through a proper foundational development of the field of tuning theory, a theory enabling the development of technique to optimize with reproducible psychoacoustic effects. 

## Theory

### Inter-harmonic Interval Alignment and the Psychoacoustics of Counterpoint

Piano tuners often analyze interval harmonic alignments by showing how all harmonics align against all others, as tables of Cartesian products in spreadsheets. However, there is usually only one harmonic that is significantly affecting the resulting beat envelope, the harmonic directly aligned. The harmonic partials of all tones have a quickly diminishing slope of harmonic amplitudes, for even a perfect square wave has a quickly diminishing slope.

The amplitude envelope has significant psychoacoustics because of the way that aural nerves are triggered by pressure potential. That is, small variations in pressure are lost in the sense organ nerve paths. One way to model the psychoacoustics mathematically is by convolving a gamma distribution function over the pressure levels. This is known as a gammatone filter, often used to model the physiology of nerves in the aural sense, which should also apply to beat amplitude envelopes.

#### The Intervalic Alignment of Larger Intervals

For each Pythagorean ratio interval, it can be theorized intuitively which harmonic would be the main driver of the beat envelope, even without analysis with a gammatone filter. 

* 2/1 perfect 8ths line up by ear along the 2nd harmonic because the 2nd harmonic lines up exactly with the fundamental of its octave.
* 3/2 perfect 5ths line up by ear along the 1st harmonic, not the 3rd, because the 3rd is weaker (-6db per octave @ 3/2 octaves is -9db weaker).
* 4/3 perfect 4ths line up by ear along the 1st harmonic, not the 4th, because the 4th is weaker (-6db per octave @ 4/2 octaves is -12db weaker).
* 5/4 major 3rds line up by ear along the 1st harmonic, not the 5th, because the 5th is weaker (-6db per octave @ 5/2 octaves is -15db weaker).
* 6/5 minor 3rds line up by ear along the 1st harmonic, not the 6th, because the 6th is weaker (-6db per octave @ 6/2 octaves is -18db weaker).

Only the 8th is significantly relevant to inharmonicity. A perfect 4th against a stretched octave and a perfect 5th is (half a cent) near a stretched even-temperament. That is, the difference of error measurement is insignificant despite the application of consonance in 5ths and 8ths. 

#### The Chorded Alignment of Smaller Intervals

The smaller a Pythagorean ratio, the more chord-centric its tuning. That is, the harmonic relationships of a minor 3rd have far more to do with how well the top note lines up with the 5th harmonic of a chord than with the harmonics of the bottom note of the minor 3rd. One of the main reasons for using stretch tuning is to maintain alignment with a chord of notes that spans the harmonic series.

#### A Fundamental-Oriented Definition of Contrapuntal Intervals

This actually leads to a definition of consonant intervals in counterpoint. The Pythagorean ratios (`(n+1)/n` - 2/1, 3/2, 4/3, 5/4, etc.) with denominators that are powers of 2 (`(2^n+1)/2^n` -- 2/1, 3/2, 5/4, 9/8, etc.) are more consonant than Pythagorean Ratios which are not (4/3, 6/5, 7/6, 8/7, etc.). The reason is because the bottom note of the ratio is phase aligned with the fundamental, and the top note phase aligns itself with the bottom note over the denominated period -- the fundamental. The result is a consonant overall phase alignment with the fundamental.

Indeed, any interval with a denominator that is a power of 2, and a numerator above the denominator, satisfies this definition, including 5/2 (C4, E5), or 9/2 (C3, D5). But try 5/3 (G4, E5) and notice the difference. That extends the definition beyond special Pythagorean ratios, into a definition based purely on the harmonic series. 

This theory is demonstrated in many ways:
1. I had developed a dynamic tuner that solved for fundamental-oriented consonance, turning chords expected to be dissonant into consonant tonal structures. 
2. 4/3 4ths would seem to be more consonant than 5/4 Major 3rds, but indeed traveling 4ths are avoided like the plague in counterpoint.
3. "Overdriven" 4ths in a "power chord" actually have a fundamental re-established by the distortion process. Distortion makes the overall wave more square, which re-shapes the harmonic structure to be re-based from the fundamental. It is a way to lower the sound of a guitar by 2 octaves from the top note. This makes the 4ths become consonant tones.

#### A New Aspect of The Distinction Between Consonant and Dissonant Intervals

This leads to a new mathematical and psychoacoustic descriptive model for the contrapuntal descriptions of intervals. And the tuning system can be optimized to satisfy these definitions of counterpoint. 

A tuning system could be designed to favor the development of a temperament for solving 8ths, 5ths, and 4ths, leaving the rest to have irrational relationships. If the 4ths and 5ths in the second octave of the harmonic series are in tune, the major and minor 3rds of the 3rd octave are less significant. This aligns with the expectations of counterpoint. 

### Inharmonicity has an Ideal Condition

There is a single global solution to an inharmonic coefficient that stretches octaves to reach the Pythagorean comma across 12 5ths of 7 stretched 8ths. 

```python
# (12 5ths / 7 8ths) for one octave == stretch tuning octave interval that aligns with the pythagorean comma
stretch_interval = ((1.5 ** 12) / (2.0 ** 7)) ** (1.0/7)
stretch_interval
1.0019377369015756

inharmonicity_coefficient_ratio = lambda harmonic, coeff: harmonic * (1.0 + 0.5 * (harmonic ** 2 - 1) * coeff)
stretch_coeff = lambda stretch_interval: (stretch_interval - 1) / 1.5
stretch_coeff(stretch_interval)
0.0012918246010504102

inharmonicity_coefficient_ratio(2, stretch_coeff(stretch_interval)) / 2
1.0019377369015756

# The stretched, even-tempered 4th, for reference
inharmonicity_coefficient_ratio(2.0 ** (5.0/12), stretch_coeff(stretch_interval))
1.3355139116958994 # stretched, even-tempered 4th
1200.0 * math.log(_ * 3 / 4) / math.log(2)
2.8290059350591482 # cents above perfect 4th

# The side-effect 4th from the 8th minus the 5th
inharmonicity_coefficient_ratio(2, stretch_coeff(stretch_interval)) / (3.0/2)
1.3359169825354342 # 4th that remains from stretched octave minus perfect 5th 
1200.0 * math.log(_ * 3 / 4) / math.log(2)
3.351430054950033 # cents above perfect 4th
```

However, there are three problems with this:
1. Pianos don't have exactly this coefficient. 
2. Temperaments usually span 1 or 2 octaves, not 7. 
3. The resulting 4th from the 8th minus the 5th.

What are the effects of assuming that the piano has the desired coefficient across a small tempered region without the desired coefficient? The coefficient is only involved in the 8ths lining up with the 2nd harmonic because the 5ths line up with the 1st harmonic. This means that 5ths are independent of the coefficient, leaving only 8ths (and therefore resulting 4ths) dependent on the coefficient.

This doesn't mean that it is not possible to abuse a 5th to help an 8th line up with a particular coefficient. The point is: why formulate the temperament for beat offsets at all? Instead of spreading out mitigations that are difficult to implement, why not distribute evenly the desired properties that are much easier to feel? The proximity of the resultant 4ths to even-temperament shows that optimized solutions can have the power of mitigation, but better converge to a solution.

That is, the psychoacoustic value of a targeted approach is logically equal to a mitigated approach, so optimize the problem toward maximum consonance value, rather than minimum dissonance error, because the "cost function" toward a maximum is far better at converging on a solution.

Consonance converges better because the beat amplitude envelope is a mathematical effect that is directly observed as a percept by the ear, but the timing of the beat amplitude envelope itself is not directly observed as a percept. The requirement of a fine-grained, absolute sense of time is a tall order for humans. As far as I know, that sense is not part of human physiology, and has to be developed 100% cognitively. 

When an optimization solution has trouble converging on a solution, it indicates a problem with an input variable. The beat rate is a bad input variable for humans without an electronic sensor to measure it properly. 

### Classes of Tuning Systems

Dissonance itself is not technically an error, but an harmonic property that is used in composition and orchestration. Tuning systems typically treat it as an error, with a design to mitigate the error. 

There are mainly two ways to deal with dissonance as an error:
1. Spread out the dissonant beats irrationally, spreading the spectrum of the noise, lowering the average amplitude of the dissonance, disrupting the beat envelop from developing a coherent shape. This is the approach of even tempering, and is generally the effect of using logarithms, even with rational comma spreads (expressed logarithmically), due to the irrational results of logarithmic functions. This has been called asynchronous tuning. 
2. Spread out the dissonant beats rationally, aligning the dissonances as a second order consonance. This is the approach of tuning by ear against integral divisions of a single tempo, or using mathematic equations and electronic tuners to the same effect. This has been called synchronous tuning. 

The beat-tempo required to implement a rational beat spread of a synchronous system is dependent on the inharmonicity coefficient, so it is very difficult to converge on a solution quickly. Interestingly, the *in*ability to rationally converge on a beat would classify the tuning as an irrational beat spread, and therefore have the psychoacoustic properties of lowering the amplitude of dissonance, the properties of an asynchronous system. Synchronous tuning is more suited to implementation on virtual instruments. 

This might explain why modern tuning practice prefers to use the error mitigation approach to achieve a stretched even-temperament, because an approximate asynchronous solution is aesthetically equal to a perfect asynchronous solution. However, the difficulty of the practice limits amateur adoption, creating an "ivory tower" mysticism of skill around the practice, but it should be possible to tune an instrument as long as there is some sense of unison. A musician should not need to hire a professional tuner. 

There is also a scientific problem with the inability to converge on a tuning. The lack of convergence violates the principle of reproducibility, lowering the descriptiveness of the medium. The RPT exam requires a master tuning as a reference, but this tuning is not reproducible, so the exam is not technically scientific.

If the RPT exam were instead a measure of ear-tuning skill, it would be an exam of self-consistency of tuning, where each examinee were to set their own master tuning, where the master tuning system were evaluated independently of tuning skill. The lack of a formal tuning theory makes it difficult to distinguish hand and ear skill from the tuning system because the theory helps define the boundaries of the tuning system, and define the precise techniques that comprise the skill. 

Regular effects are important for compositional design. A composition may only be designed for a particular temperament when its effects are repeatable. As a composer, I have abused awkward regularities in virtual instruments that are not real properties of the physical instrument. It is extremely important for the musician to have precise control over the instrument. 

Tuning systems have 3 demands, that they be:
1. Aesthetically aligned: that consonance of all degrees is output, since it is a better effect.
2. Rationally aligned: that consonance of the 1st degree is input, since it is easier to affect. 
3. Evenly tempered: that consonance is regularly available from any musical condition, increasing expressive power.

A theorem could be stated that only 2 out of the 3 of the demands may be satisfied at any time. But as in any problem of entropy, the optimal solution involves directing the flow of thermodynamic energy through a system. The system is to be broken down into problem domains, and the demand pressures are to be guided through system components.

The PATH tuning system proposes a hybrid tuning system where 8ths, 5ths, and 4ths are controlled rationally, but remaining intervals, and stretch-gaps are left to logarithmic effects. This takes advantage of the properties of both even tempering and rational tuning, and most importantly, incorporates arbitrary inharmonicity as a design condition.

In PATH, a rational component is separated from an irrational component. The rational component satisfies demands 1 and 2, and the irrational component satisfies demands 1 and 3. In each case, demand 1 is satisfied, the aesthetic demand of the listener, leaving the tuner to balance the demands across 2 and 3, but this balance is defined by PATH in a formal way, where demand 3 is implied by the way that demand 2 is implemented. 

### Inharmonicity in Non-Ideal Conditions

No matter what the inharmonicity, tuning 5ths against the 1st harmonic has a constant ideal aesthetic effect. However, maintaining that ideal assumes that 8ths will be able to stretch back across the 5ths spanning the ideal inharmonicity coefficient.

In theory, all notes can be tuned with just 5ths in a single direction, creating 7 parallel chains of 5ths that are only orthogonal (independent) along the 5ths. These chains can be identified by a modulo 7 against the note number, 0 through 6 (`N % 7`). For example, chains of 3 5ths:
```txt
0: C4, G4, D5
1: C#4, G#4, D#5
2: D4, A4, E5
3: D#4, A#4, F5
4: E4, B4, F#5
5: F4, C5, G5
6: F#4 C#5, G#5
```

That orthogonality can be seen by unrolling the table columns:
```txt
0: C4 - 1st link of each chain
1: C#4
2: D4
3: D#4
4: E4
5: F4
6: F#4
0: G4 - 2nd link of each chain
1: G#4
2: A4
3: A#4
4: B4
5: C5
6: C#5
0: D5 - 3rd link of each chain
1: D#5
2: E5
3: F5
4: F#5
5: G5
6: G#5
```

#### General Theory of Connecting Interval Chains

A tuning system may be described simply as a function that takes a single parameter of a note, and returns a frequency. That is not necessarily even the case, since other parameters may be used, like musical context, or instrument properties. More generally, a tuning system is a system for tuning the pitches of notes. 

The possible scope of theory for tuning systems is vast. There are a lot of observations about it, and a variety of techniques, but not a lot of *descriptive* theory. Even the mathematics of tuning have trouble relating to specific aesthetic effects. 

Parallel orthogonal chains of any interval may be created. Most tuning systems are based on allocating intervals within an octave. If all octaves are constrained to the same ratio, that leaves 12 "chains" of octaves. For example, all C notes are one chain, and all C# notes are a second chain, and so on, until reaching another C. 

PATH uses 5ths (modulo 7). A second order interval to intersect, and thereby connect, the non-factoring chains logically expresses the comma-spreads between each chain.

PATH is based on chains of 5ths instead of octaves. 5ths are 7 notes apart, meaning that 7 independent chains exist. The same is possible with 4ths and 5 independent chains. Each has different properties and side-effects to be considered.

PATH uses 8ths (modulo 12) to connect the 5ths (modulo 7). 

One way to spread the Pythagorean comma is to use a 1st-order chain of 8ths, and a 2nd-order chain of 5ths, beat counting a circle of 5ths against a tempo that happens to line up with a starting note, and the inharmonicity of the instrument. But PATH shows that you can swap the orders, and connect 8ths purely, in a way that distributes the comma in a self-similar leaf pattern. 

PATH connects by 8ths. A note of `N % 7` connects to a note `(N - 8) % 7`, equal to `(N + 2) % 7`. A circle of chains connected by 8ths is therefore `[0, 2, 4, 6, 1, 3, 5]`. For example:
```txt
0, 2: D5, D4
1, 3: D#5, D#4
2, 4: E5, E4
3, 5: F5, F4
4, 6: F#5, F#4
5, 0: G5, G4
6, 1: G#5, G#5
```

In circle sequence, moving 5ths to keep within the table range, as an example:
```txt
0, 2: D5, D4
Up 2 5ths
2, 4: E5, E4
Up 2 5ths
4, 6: F#5, F#4
Up 2 5ths
6, 1: G#5, G#4
Up 1 5th
1, 3: D#5, D#4
Up 2 5ths
3, 5: F5, F4
Up 2 5ths
5, 0: G5, G4
```
In fact, the number of 5ths moved is arbitrary. For example, not moving 5ths at all, and moving from D4 to D3 also moves from chain 2 to chain 4. 

This means that any 7 chains of 5ths can have 7 random (arbitrarily tuned) 8ths connecting them, as long as each 8th connects to a distinct chain connected to no other 8th. However, the ratio between each chain would vary depending on the distance away from the ideal inharmonicity coefficient of the stretch of each 8th. That is, if the ideal coefficient is used, the ratios between each respective chain will be equal, and all ratios will be per-interval constant, a perfect even-stretch temperament.

#### Beat Effects on Lower Harmonic Intervals

For inharmonicity coefficients below the ideal coefficient, the speed of the beats between the 8ths and the 4ths are inverse-proportional to each other. That is, the ideal coefficient has perfect 8ths, and a coefficient of 0 has perfect 4ths, and there is a gradient between them. Most pianos have very small coefficients in the midrange, but 8ths tend to be orchestrated in the outer ranges. This also means that the chains of 5ths will drift away from even pitch distribution, greatly affecting the intervals not yet defined, favoring short chains, lowering the total comma-drift across the edges of the chains. 

The same situation happens in typical Pythagorean comma spreads of 1st-order 8ths and 2nd-order 5ths, but the 4ths and 5ths have the swapping gradients, instead of 4ths and 8ths. The same thing can be done with 8ths and Major 3rds, but a 3rd order of chains would be required, because the 2nd-order modulo 4 is a factor of the 1st-order modulo 12, so it would not fully connect to the 1st order. Also, using a 2nd-order modulo that factors into the 1st-order modulo creates a fixed period of effects of the 2nd-order within the 1st-order. For example, a Major 3rd pattern within an 8th repeats the Major 3rd pattern (modulo 4) 3 times within the 8th (modulos 12/4=3).

It is possible to use a 1st-order of 4ths, and a 2nd-order of 8ths, but that lowers the number of 8ths over which to spread the comma, requiring a much higher inharmonicity coefficient. However, using 4ths would mean that only 5 parallel chains would need to optimized, rather than 7 for 5ths. That is, 5ths have less drift than 4ths, since the 5th circle spans a greater distance.  

#### Beat Effects on Higher Harmonic Intervals

So far in the definition of PATH, there are definitions for 8ths, 5ths, and the resulting 4ths. All other intervals are undefined at this point. Defining 8ths and 5ths also implicitly defines 4ths. Theoretically, any modulo A against modulo B also implicitly defines modulo A-B, wherever the modulo B connects. 

In non-ideal inharmonicity conditions, an interesting property emerges from the non-equality of the smaller intervals: the logarithmic effects of differences in inharmonicity create logarithmic, irrational distributions of the smaller intervals, gaining the benefit of shaping the dissonant noise, lowering its average amplitude. That is, the imperfections are moved to where they benefit the solution. This may seem similar to "noise shaping", but it is even better, because the noise is part of the solution. 

### Even Consonance Distribution via Self-Similarity

The system so far may be thought of as a functional medium with input variables and output variables. 

The input variables are:
1. The lengths of the chains of 5ths (which 5ths are unchained).
2. Where the distinct 8th connections are made.
3. The inharmonic properties of the instrument. 

The output variables are:
1. The span of the gradients between the 4ths and 8ths, which span the 5th chains, and the resulting gradients from the inharmonicity of the instrument.
2. The variations in the pitches of the smaller intervals, against the logarithmic inharmonic properties of the instrument.
3. The sparse errors in 8ths, 5ths, and 4ths along the 5th-chain and 8th-connection boundaries. 

Due to the gradient effects of non-ideal inharmonicity, an implementation should use short chains. The shortest chain-connection pattern possible is 2 5ths up, and 1 8th down. So a temperament "leaf" can be created from that. Then a "trunk" of 8ths can connect several leaf temperaments in a self-similar pattern. 

Self-similar patterns are known for being mathematically ideal for distributing effects evenly. For example:
- The constant ratio of even tempering is a self-similar pattern.
- A "Poisson process" is a self-similar pattern.
- A fractal antenna can use a Hilbert curve to increase the distribution of the frequency sensitivity of the antenna; that is to increase the bandwidth. 
- In Geographic Information Systems, spatial databases use self-similar spatial curves to temper access times against spatial data.
- In information theory, self-similarity lowers entropy by definition. Similarly, the bandwidth of dissonance is increased, spreading the entropy across a band of frequencies.

## Method

### The Middle Temperament Leaf

First, create the smallest connected series of chains possible. Move ascending in 5ths against the 1st harmonic, and descend in octaves against the second harmonic, only to not-yet-tuned modulo-7 (perfect 5th) intervals. This creates a temperament "leaf node". 

```csv
Interval, Note, Chain, Segment, Memo
,,,,3rd Temperament Leaf
Unison, C4, 0, 3,
Down, F3, 0, 3, Down a 5th
Unison, C4, 0, 3,
Up, G4, 0, 3,
Down, G3, 2, 3,
Up, D4, 2, 3,
Up, A4, 2, 3,
Down, A3, 4, 3,
Up, E4, 4, 3,
Up, B4, 4, 3,
Down, B3, 6, 3,
Up, F#4, 6, 3,
Down, F#3, 1, 3,
Up, C#4, 1, 3,
Up, G#4, 1, 3,
Down, G#3, 3, 3,
Up, D#4, 3, 3,
Up, A#4, 3, 3,
Down, A#3, 5, 3,
Up, F4, 5, 3,
```

F3-B4 are now tuned, in 3 contiguous groups of notes:
1. the 7 notes from F3 to B3,
2. the 5 notes from C4 to E4, 
3. the 7 notes from F4 to B4.

The 5th chains are:
- 0: F3, C4, G4
- 2: G3, D4, A4
- 4: A3, E4, B4
- 6: B3, F#4
- 1: F#3, C#4, G#4
- 3: G#3, D#4, A#4
- 5: A#3, F4

The 8th connections are:
- 0, 2: G4, G3
- 2, 4: A4, A3
- 4, 6: B4, B3
- 6, 1: F#4, F#3
- 1, 3: G#4, G#3
- 3, 5: A#4, A#3

The 8th tunings cross from octave 4 to 3, from F to B, connecting each chain 0-6, so the 2nd harmonic of the 1st group is bound to the 1st harmonic of the 3rd group. The 2nd group is bound by 5ths at the 1st harmonic to the 1st group. 

That establishes the middle temperament.

### Temperament Leaves

Placing such temperaments contiguously against each other is the following series of ranges:
1. D0-A1 (from A#0)
2. A#1-E3 (from F2)
3. F3-B4 (from C4)
4. C5-F#6 (from G5)
5. G6-C#8 (from D7)

The 2nd, 3rd (middle), and 4th temperaments can be implemented similarly. The 5th temperament just needs to work around the missing C#, which is trivial. The 1st temperament is impractical. That should just be A0-A1 tuned by 8ths from A2, descending. 

Note that each temperament leaf is not actually a copy of other leaves. Although each leaf uses the same method, due to differences in inharmonicity, the results are different, and tailored to each temperament range. The ratios between corresponding chains of 5ths vary in each leaf. That is, the ratio between chain 1 and 2 in the 4th temperament may differ from the ratio between chain 1 and 2 in the 3rd temperament, because the inharmonicity coefficient may vary. That is by design.

That is a benefit of the recursion in the method, rather than the recursion of the results of a single temperament. The method can be recursed because it is actually no more complex than extrapolating a reference temperament because consonance is being measured either way. 

### Trunking the Leaves

The starting note of each leaf is the 8th lowest note. The 3rd temperament starts at C4, the 8th note above F3, its lowest note. Each contiguous temperament needs to be connected to the neighboring temperaments in some way. Connecting by a 5th would have a side effect of connecting two 5th chains together, but a design requirement is that the 5th chains be a short as possible. Therefore, temperaments should be connected by 8ths.

Connecting to the first chain in a sequence by an 8th is free, interfering with no other aspects of the tuning. So, connect the 8th inward toward to the 3rd temperament to the starting note of each other temperament.

However, each temperament flexes the widths in between its 5th chains to accommodate differences in inharmonicity coefficient across the keyboard. There are 8ths connecting within a temperament range, but the other 8ths are disconnected, so the end of a sequence can drift significantly from the beginning of a sequence. That can happen even from just small errors in tuning.

The typical solution is to extend 8ths from a single reference tuning, and rely on check-tuning to keep the non-8ths acceptable. Recall that, in PATH, 8th connections can be arbitrarily placed as long as the constraint is satisfied that each 5th chain can only have a single intersecting 8th. So instead of only connecting 8ths within a small area, the 8th connections within a temperament can be staggered, odd 8ths connecting from outside the temperament, and even 8ths connecting within the temperament.

The tuning system can be seen as a graph of tunings connecting each interval. PATH limits this graph to consonant 5ths and 8ths. In this view, the staggered connections have the effect of limiting the distance of tuned interval edges connecting the intervals. Check-tuning can be seen as adding more edges beyond what is rationally possible to align with consonance, whereas PATH simply optimizes the consonant tuning paths between intervals. 

Each 8th connection that staggers from outside the temperament can be placed anywhere on the chain to which it connects (as a sink, forward in the progression). That provides some ambiguity, or variability, in the connections. These links should be made where the tuning paths are shortest. That is likely the middle link of the chain. 

### Chains and Connections

5th Chain Legend:
- chain-modulo: note-link, note-link[, ...]
- `note>`: 8th connection source up
- `note->`: 8th connection source up to another temperament 
- `<note`: 8th connection source down
- `<-note`: 8th connection source down to another temperament
- `note<`: 8th connection sink up
- `>note`: 8th connection sink down
- `note<-`: 8th connection sink up from another temperament
- `->note`: 8th connection sink down from another temperament
- `!note`: reference note, counts as a sink

8th Connection Legend:
- from-modulo, to-modulo: from-note, to-note

Connection Constraints:
- Each 5th chain must have one and only one sink connection.
- Each 5th chain may have any number of source connections. 

#### 1st Temperament

There are no 5th chains. A full temperament is not practical here.

The 8th connections:
- 6, -: A2, A1
- 5, -: G#2, G#1
- 4, -: G2, G1
- 3, -: F#2, F#1
- 2, -: F2, F1
- 1, -: E2, E1
- 0, -: D#2, D#1
- 6, -: D2, D1
- 5, -: C#2, C#1
- 4, -: C2, C1
- 3, -: B1, B0
- 2, -: A#1, A#0
- -, -: A1, A0

#### 2nd Temperament

The 5th chains are:
- 2: `<-A#1`, `<-F2<-`, `<C3`
- 4: `<-C2<`, `<-G2`, `D3`
- 6: `<-D2`, `<-A2<-`, `<E3`
- 1: `<-E2<`, `B2`
- 3: `<-B1`, `<-F#2<-`, `<C#3`
- 5: `<-C#2<`, `<-G#2`, `D#3`
- 0: `<-D#2`, `A#2<-`

The 8th connections:
- 0, 2: F3, F2
- 2, 4: C3, C2
- 4, 6: A3, A2
- 6, 1: E3, E2
- 1, 3: F#3, F#2
- 3, 5: C#3, C#2
- 5, 0: A#3, A#2

#### 3rd Temperament

The 5th chains are:
- 0: `<-F3`, `!C4`, `<G4->`
- 2: `G3<`, `D4`, `<A4`
- 4: `<-A3<`, `E4->`, `<B4`
- 6: `B3<`, `<F#4`
- 1: `<-F#3<`, `C#4->`, `<G#4`
- 3: `G#3<`, `D#4`, `<A#4`
- 5: `<-A#3<`, `F4->`

The 8th connections are:
- 0, 2: G4, G3
- 2, 4: A4, A3
- 4, 6: B4, B3
- 6, 1: F#4, F#3
- 1, 3: G#4, G#3
- 3, 5: A#4, A#3

#### 4th Temperament

The 5th chains are:
- 5: `C5->`, `->G5`, `<D6->`
- 0: `D5<`, `A5`, `E6`
- 2: `->E5`, `B5->`, `<F#6`
- 4: `F#5<`, `C#6`
- 6: `->C#5`, `G#5->`, `<D#6`
- 1: `D#5<`, `A#5`, `F6`
- 3: `->F5`, `C6->`

The 8th connections are:
- 0, 5: C4, C5
- 5, 0: D6, D5
- 4, 2: E4, E5
- 2, 4: F#6, F#5
- 1, 6: C#4, C#5
- 6, 1: D#6, D#5
- 5, 3: F4, F5

#### 5th Temperament

The 5th chains are:
- 3: `G6`, `->D7`, `<A7`
- 5: `A6<`, `E7`, `B7`
- 0: `->B6`, `F#7`, (`<C#8`)
- 2: `C#7<`, `G#7`
- 4: `->G#6`, `D#7`, `<A#7`
- 6: `A#6<`, `F7`, `C8`
- 1: `->C7`, `G7`

The 8th connections are:
- 5, 3: G5, G6
- 3, 5: A7, A6
- 2, 0: B5, B6
- 0, 2: C#8 (via F#7), C#7
- 6, 4: G#5, G#6
- 4, 6, A#7, A#6
- 3, 1: C6, C7

### Recurse the 2nd, 4th, and 5th Temperament Leaves.

4rd temperament leaf:
```csv
Interval, Note, Chain, Segment, Memo
,,,,4th Temperament Leaf
Unison, G4, 0, 3,
Up, G5, 5, 4, Up an 8th
Down, C5, 5, 4, Down a 5th
Unison, G5, 5, 4,
Up, D6, 5, 4,
Down, D5, 0, 4,
Up, A5, 0, 4,
Up, E6, 0, 4,
Unison, E4, 4, 3,
Up, E5, 2, 4, Up an 8th
Up, B5, 2, 4,
Up, F#6, 2, 4,
Down, F#5, 4, 4,
Up, C#6, 4, 4,
Unison, C#4, 1, 3,
Down, C#5, 6, 4, Up an 8th
Up, G#5, 6, 4,
Up, D#6, 6, 4,
Down, D#5, 1, 4,
Up, A#5, 1, 4,
Up, F6, 1, 4,
Unison, F4, 5, 3,
Down, F5, 3, 4, Up an 8th
Up, C6, 3, 4,
```

2nd temperament leaf:
```csv
Interval, Note, Chain, Segment, Memo
,,,,4th Temperament Leaf
Unison, F3, 0, 3,
Down, F2, 2, 2,
Down, A#1, 2, 2, Down a 5th
Unison, F2, 2, 2,
Up, C3, 2, 2,
Down, C2, 4, 2,
Up, G2, 4, 2,
Up, D3, 4, 2,
Unison, A3, 4, 3,
Down, A2, 6, 2,
Down, D2, 6, 2, Down a 5th
Unison, A2, 6, 2,
Up, E3, 6, 2,
Down, E2, 1, 2,
Up, B2, 1, 2,
Unison, F#3, 1, 3,
Down, F#2, 3, 2,
Down, B1, 3, 2, Down a 5th
Unison, F#2, 3, 2,
Up, C#3, 3, 2,
Down, C#2, 5, 2,
Up, G#2, 5, 2,
Up, D#3, 5, 2,
Unison, A#3, 5, 3,
Down, A#2, 0, 2,
Down, D#2, 0, 2, Down a 5th
```

5th temperament leaf, skip the C#8:
```csv
Interval, Note, Chain, Segment, Memo
,,,,4th Temperament Leaf
Unison, D6, 5, 4,
Up, D7, 0, 5, Up an 8th
Down, G6, 0, 5,
Unison, D7, 0, 5,
Up, A7, 0, 5,
Down, A6, 2, 5,
Up, E7, 2, 5,
Up, B7, 2, 5,
Unison, B5, 2, 4,
Up, B6, 4, 5, Up an 8th
Up, F#7, 4, 5, Tune C#7 via this note.
Up, C#8, 4, 5, This note does not exist...
Down, C#7, 6, 5, ...so go down a 4th from F#7, or an 8th from C#6
Up, G#7, 6, 5,
Unison, G#5, 6, 4,
Up, G#6, 1, 5, Up an 8th
Up, D#7, 1, 5,
Up, A#7, 1, 5,
Down, A#6, 3, 5,
Up, F7, 3, 5,
Up, C8, 3, 5,
Unison, C6, 3, 4,
Up, C7, 5, 5, Up an 8th
Up, G7, 5, 5,
```

### The Bottom Octave

At this point, the range A0-A1 are left. The harmonics are more complex on these wider strings with brighter tones. Just tune from top to bottom, from A1 to A0, using 8ths from A2 to A1. A1 will then be tuned by the time A0 is tuned. It would be much harder to tune 5ths this low, 8ths being hard enough to hear. And music going this low will more likely line up on 8ths than 5ths. 

```csv
Interval, Note, Chain, Segment, Memo
Unison, A2,,,
Down, A1,,,
Unison, G#2,,,
Down, G#1,,,
Unison, G2,,,
Down, G1,,,
Unison, F#2,,,
Down, F#1,,,
Unison, F2,,,
Down, F1,,,
Unison, E2,,,
Down, E1,,,
Unison, D#2,,,
Down, D#1,,,
Unison, D2,,,
Down, D1,,,
Unison, C#2,,,
Down, C#1,,,
Unison, C2,,,
Down, C1,,,
Unison, B1,,,
Down, B0,,,
Unison, A#1,,,
Down, A#0,,,
Unison, A1,,,
Down, A0,,,
```

All 88 keys should now be in tune. 
