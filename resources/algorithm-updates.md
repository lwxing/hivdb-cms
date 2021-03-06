## Version 8.9 update 2019-10-07

The 8.9 drug resistance ASI file is downloadable at [here][asi89].

We upgraded scores and comments for NNRTI (doravirine and rilpivirine) and INSTI drugs (bictegravir, dolutegravir, elvitegravir and raltegravir) based on recent studies [^GenoPheno][^Rhee2019].

The latest comments for NNRTI and INSTI drug resistance mutations can be found at [here](/dr-summary/comments/NNRTI/) and [here](/dr-summary/comments/INSTI/).

All changed rules and affected patterns are listed in [this document][asi89changes].

### Version 8.9-1 update 2019-11-01

We upgraded the ASI file to ASI format 2.2, which requires ASI Interpreter >1.5.0.1. No change was made to the 8.9 rules or mutation comments. However, we do include "drug-level" comments through the new ASI syntax.

The 8.9-1 drug resistance ASI file is downloadable at [here][asi89p1].

[^GenoPheno]: Genotype-Phenotype Datasets. [Stanford HIVDB](https://hivdb.stanford.edu/pages/genopheno.dataset.html) (2019).
[^Rhee2019]: Rhee SY, Grant PM, Tzou PL, Barrow G, Harrigan PR, Ioannidis JPA, Shafer RW. A systematic review of the genetic mechanisms of dolutegravir resistance. [J Antimicrob Cng hemother](https://hivdb.stanford.edu/pages/pdf/Rhee.2019.JAC.pdf) (2019).

## Version 8.8 update 2019-02-13

The 8.8 drug resistance ASI file is downloadable at [here][asi88].

In this version, several rule changes regarding to the INSTI drugs (especially DTG) were introduced and the INSTI comments have also been updated correspondingly.

All changed rules and affected patterns are listed in [this document][asi88changes].

## Version 8.7 update 2018-10-19

The 8.7 drug resistance ASI file is downloadable at [here][asi87].

Three types of change are included in this release:

1. New scores for the recently approved NNRTI drug doravirine (DOR);
2. Updated NNRTI comments for DOR; and
3. Minor score tweaks for INSTI drugs bictegravir (BIC) and dolutegravir (DTG) in reflect to a [recently published study](https://academic.oup.com/ofid/article/5/10/ofy221/5092934).

All changed rules and affected patterns are listed in [this document][asi87changes].

## Version 8.6 update 2018-07-03

The 8.6 drug resistance ASI file is downloadable at [here][asi86].

This is a minor release version which made several score changes to INSTI drugs bictegravir (BIC), dolutegravir (DTG), elvitegravir (EVG), and raltegravir (RAL). All changed rules and affected patterns are listed in [this document][asi86changes].

### Version 8.6.1 update 2018-07-18

The 8.6.1 drug resistance ASI file is downloadable at [here][asi86a].

PIs and INSTIs comments are updated in this version. Additional comments are added for following mutations:

1. PR 33-41 insertions
2. IN 50I, 74F, 119R, 142T, and 149A

No score rules are changed in this version.

## Version 8.5 update 2018-04-16

The 8.5 drug resistance ASI file is downloadable at [here][asi85].

In February 2018, Bictegravir (BIC) was approved as part of a fixed dose formulation in combination with TAF/FTC (Biktarvy). Preliminary data from published studies of site-directed mutants and clinical isolates suggests that the resistance profile of BIC is similar to that of DTG [^Andreatta2018][^Tsiang2016]. Supporting data from a recent review and from data in macaques also support these preliminary data [^Hassounah2017][^Anstett2017]. There are no published data yet of virological failures with resistance on BIC because it has been used in far fewer patients than DTG and because it has not been used in patients who have failed other INSTIs. In addition, it has always been used as part of a fixed-dose combination rather than as monotherapy. The comments and INSTI notes pages will be updated within the month to reflect recent INSTI resistance studies and the approval of bictegravir.

[^Andreatta2018]: Andreatta K, Chang S, Martin R, Willkom M, White K. 2018. Integrase inhibitor resistance selections initiated with drug resistant HIV-1 \[Poster 546\]. [CROI 2018](http://www.croiconference.org/sites/default/files/posters-2018/1430_Andreatta_546.pdf) ([Data](/cgi-bin/Reference.cgi?RefID=2591)).
[^Tsiang2016]: Tsiang M, Jones GS, Goldsmith J, Mulato A, Hansen D, Kan E, Tsai L, Bam RA, Stepan G, Stray KM, Niedziela-Majka A, Yant SR, Yu H, Kukolj G, Cihlar T, Lazerwith SE, White KL, Jin H. 2016. Antiviral Activity of Bictegravir (GS-9883), a Novel Potent HIV-1 Integrase Strand Transfer Inhibitor with an Improved Resistance Profile. [Antimicrob Agents Chemother 60:7086-7097](http://www.ncbi.nlm.nih.gov/pubmed/27645238) ([Data](/cgi-bin/Reference.cgi?RefID=2592)).
[^Hassounah2017]: Hassounah SA, Alikhani A, Oliveira M, Bharaj S, Ibanescu RI, Osman N, Xu HT, Brenner BG, Mesplede T, Wainberg MA. 2017. Antiviral Activity of Bictegravir and Cabotegravir against Integrase Inhibitor-Resistant SIVmac239 and HIV-1. [Antimicrob Agents Chemother 61](http://www.ncbi.nlm.nih.gov/pubmed/28923862).
[^Anstett2017]: Anstett K, Brenner B, Mesplede T, Wainberg MA. 2017. HIV drug resistance against strand transfer integrase inhibitors. [Retrovirology 14:36](http://www.ncbi.nlm.nih.gov/pubmed/28583191).

## Version 8.4 update 2017-06-16

The 8.4 drug resistance ASI file is downloadable at [here][asi84].

This is a minor release version which made several score changes to PI drug atazanavir/r (ATV/r):

1. For ATV/r, a resistance score of 10 instead of 0 was contributed by protease DRM I47V.
2. For ATV/r, a resistance score of 5 instead of 0 was contributed by the combination of protease DRMs at positions 32 + 47, 32 + 54 or 47 + 54.

Download the rule comparison between 8.3 and 8.4 [here][asi84changes].

## Version 8.3 update 2017-03-02

The 8.3 drug resistance ASI file is downloadable at [here][asi83].

This is a minor release version which made several changes related with the comments:

1. The "dosage considerations" were changed to base on drug resistance levels, not mutations. Specifically, dosage comment for high-level DRV/r resistance and intermediate/low-level TPV/r resistance is only displayed when TPV/r is hidden from the report. Due to the limitation of ASI program, we excluded those comments from our ASI XML file. You can find the dosage comments at the [Drug Resistance Summary pages](/dr-summary/comments/PI/).
2. A new comment for RT68G (NRTI Other) was added.
3. Other minor changes to existing comments were applied.

Internally, we introduced a new "conditional comments" module for allowing comments not related with mutations (but with drug resistance levels). The Sierra GraphQL interface was changed slightly too, several fields were added, other several fields were deprecated but still accessiable.

## Version 8.2 update 2016-12-09

The 8.2 drug resistance ASI file is downloadable at [here][asi82].

This is a minor release version which adjusted following scores:

1. For NRTI drug abacavir (ABC), an extra score of 20 was applied to the combination of RT DRMs at positions 67, 70, 184 and 219. This addition was based on an ongoing polling of 16 experts in HIV drug resistance which will be described in more detail later this month.
2. For NRTI drug abacavir (ABC), the score for the combination of RT DRMs at positions 41 and 215 was increased from 10 to 15. This addition was based on an ongoing polling of 16 experts in HIV drug resistance which will be described in more detail later this month.
3. For INSTI drugs elvitegravir (EVG) and raltegravir (RAL), the scores of existing rules for G163R/K were increased from 10 to 15 based on user feedback.

This version also introduced a new type of mutation comments called "Dosage Considerations". A PI comment and a INSTI comment, which provide drug dosage recommendations, were added to this type.

## Version 8.1 update 2016-09-15

The 8.1 drug resistance ASI file is downloadable at [here][asi81].

The changes were made to the HIVDB genotypic resistance interpretation system since the last update reflect (i) trends in ARV treatment strategies, (ii) additional knowledge about specific drug-resistance mutations (DRMs), and (ii) the expanded use of genotypic testing outside of upper-income countries:

1. Mutation classification:
   1. PR and IN DRMs are now classified as “Major”, “Accessory”, and “Other” rather than “Major”, “Minor”, and “Other”. RT DRMs are still classified as “NRTI”, “NNRTI”, and “Other”.
   2. Nearly all mutations classified as Major or Accessory (for PR or IN), NRTI, or NNRTI have mutation penalty scores. Exceptions are made only for highly unusual amino acids at important drug-resistance positions for which no published data are available. These mutations are not classified as “Other” so that they can be displayed more prominently. Such mutations are accompanied by a comment summarizing the effects of the usual DRMs at this position but indicating that there are no data for the particular observed amino acid.
   3. Nearly every mutation with a mutation penalty score, even those that have scores only when they occur in combination with other mutations, are classified as “Major” or “Accessory” (for PR or IN) or NRTI or NNRTI. Currently, there are only two exceptions:
      1. The highly polymorphic IN mutations L74M/I are classified as “Other” even though they do have mutation penalty scores when they occur with Q148H/R/K or Y143C/R/H/S/G/A.
      2. The polymorphic RT mutation K103R is classified as “Other” even though it has a mutation penalty score when it occurs in combination with V179D.
   4. Several polymorphic mutations no longer receive penalty scores and have been reclassified as “Other”:
      1. The somewhat polymorphic NRTI mutations T69N and V118I.
      2. The highly polymorphic PR mutations K20I and T74S which previously had low mutation penalty scores for NFV.
      3. The minimally polymorphic mutation E35G which previously had a low mutation penalty score for TPV.
   5. Several new mutations were added
      1. The extremely rare RT deletions at codons 68 and 70.
      2. The extremely rare IN mutation Q148N.
2. Mutation scoring
   1. Many changes were made to the individual and combination mutation penalty scores. Every score change is indicated in the accompanying drug class RulesComparison.V7\_0.vs.V8\_0.tsv files.
   2. The impact of these changes on thousands of the most common distinct DRM patterns for each class is indicated in the accompanying drug class PatternsComparison.V7\_0.vs.V8\_0.tsv files. The DRM patterns in these files are sorted in order of their frequency.
3. Comments  
   Each of the Mutation Comments has been updated for brevity, clarity, and to reflect new knowledge as detailed in the Resistance Notes
4. Resistance Notes  
   The NRTI, NNRTI, PI, and INSTI notes pages have been updated with 176, 91, 89, and 69 references, respectively.

### Version 8.1.1 update 2016-09-23

The 8.1.1 drug resistance ASI file is downloadable at [here][asi81a].

This is a bugfix version which fixed several issues related with comments. No score rules are touched.

1. Add back the comments to classic Sierra.
2. A few comments was slightly changed.
3. A new faster algorithm implementation was adopted. The score results of both are identical.

[asi81]: $$CMS_PREFIX$$downloads/asi/HIVDB_8.1.xml
[asi81a]: $$CMS_PREFIX$$downloads/asi/HIVDB_8.1.1.xml
[asi82]: $$CMS_PREFIX$$downloads/asi/HIVDB_8.2.xml
[asi83]: $$CMS_PREFIX$$downloads/asi/HIVDB_8.3.xml
[asi84]: $$CMS_PREFIX$$downloads/asi/HIVDB_8.4.xml
[asi85]: $$CMS_PREFIX$$downloads/asi/HIVDB_8.5.xml
[asi86]: $$CMS_PREFIX$$downloads/asi/HIVDB_8.6.xml
[asi86a]: $$CMS_PREFIX$$downloads/asi/HIVDB_8.6.1.xml
[asi87]: $$CMS_PREFIX$$downloads/asi/HIVDB_8.7.xml
[asi88]: $$CMS_PREFIX$$downloads/asi/HIVDB_8.8.xml
[asi89]: $$CMS_PREFIX$$downloads/asi/HIVDB_8.9.xml
[asi89p1]: $$CMS_PREFIX$$downloads/asi/HIVDB_8.9-1.xml
[asi84changes]: $$CMS_PREFIX$$downloads/hivdb-changes/HIVDB_8.4.changes.zip
[asi86changes]: $$CMS_PREFIX$$downloads/hivdb-changes/HIVDB_8.6.changes.pdf
[asi87changes]: $$CMS_PREFIX$$downloads/hivdb-changes/HIVDB_8.7.changes.pdf
[asi88changes]: $$CMS_PREFIX$$downloads/hivdb-changes/HIVDB_8.8.changes.pdf
[asi89changes]: $$CMS_PREFIX$$downloads/hivdb-changes/HIVDB_8.9.changes.pdf
