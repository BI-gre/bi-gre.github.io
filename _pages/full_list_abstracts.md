---
layout: page
title: Bigre days: Talks & posters 
permalink: /days/abstracts
---


## Talks

### Predicting coarse-grained representations of biogeochemical cycles from metabarcoding data

*by Belcour Arnaud, Inria*

Motivation: Microbial communities can have critical impact on their environments (human health, soil, marine or industrial storage). Taxonomic identification of these communities is now routinely performed thanks to advance in DNA sequencing (with metabarcoding and metagenomics). Determine their functional potential (such as degrading metabolites or producing toxins) is a key element to understand their impact. Direct inference of these functions can be performed with metagenomics (sequencing of all DNA in the sample). But this requires a quantity of DNA that is not always available, such as in salt caverns. It is then only possible to make estimation from the taxonomic composition and using closely related public genomes. But these methods often rely on one specific gene marker (such as 16S rRNA gene), lack intermediary explanation on how the predictions are performed and output large quantity of functions, sometimes difficult to interpret.

Results: We developed a pipeline, called Tabigecy, predicting functions of biogeochemical cycles from taxonomic affiliations. In a first step, Tabigecy uses EsMeCaTa to predict consensus proteomes from the input affiliations. To optimise this process, we created a precomputed database containing information for 2,404 taxa of UniProt. Theses consensus proteomes are searched using bigecyhmm, a newly developed Python package, relying on Hidden Markov Models to identify key enzymes involved in biogeochemical cycles. These functions are then represented into coarse-grain representation of these cycles. We applied Tabigecy to two salt cavern datasets to compare its predictions to the datasets culture and hydrochemistry measurements performed. These results highlighted the usefulness of the method in providing an overview of the metabolism present in microbial communities.

Availability: The Tabigecy pipeline is available at https://github.com/ArnaudBelcour/tabigecy.

### Two-dimensional numerical resolution of a polar active matter model applied to collective cell migration


*by Shourick Nathan, INRAE - Piaf*

Collective cell migration contributes to embryogenesis, wound healing and tumour metastasis. Several cases of continuous modelling of collective cell migration have been studied in the literature: collective movement in a confined circular space, periodic migration and strip migration. Most of these studies present 2D experiments and some have proposed 2D modelling. However, in most cases, the chosen geometries lead only to 1D spatial heterogeneities and these models have only been solved in 1D. In fact, no modelling studies with full 2D heterogeneities have yet been carried out. The aim of this talk is therefore to fill this gap by solving a polar active matter model on a two-dimensional geometry. For this purpose, we use a Stokes experiment carried out by our biophysicist colleagues, which generates a heterogeneous flow by forcing the cells to go around a circular obstacle, making it possible to discriminate between models. This presentation will focus on stationary solutions and the effects of dimensionless model parameters on model dynamics. A comparison between numerical calculations and experimental data will also be proposed.


### Peritumoral tissue is a promising source of prognostic biomarkers


*by KOCA Dzenis, CEA IRIG*

Traditional medicine often employed a "one treatment fits all" approach, wherein patients were treated based on displayed symptoms. The advent of digital technologies and advancements in data collection, storage, analysis, and comprehension, particularly in cancer science, holds the promise of a more personalized approach to treatment, known as precision medicine. The premise of precision medicine, primarily with regard to cancer, is that treatment should be tailored to more precisely fit the patient. One of the cornerstones of precision medicine lies in accurate risk assessment, mirrored in the correct prognosis of the patient's outcome. The result of correct risk assessment is a treatment that reflects the severity of the disease.
While emerging survival prediction models mostly rely on clinical information (tumor stage, grade,...) supplemented with genomic data from tumors, many of these models struggle to transition to the clinical setting. This limited success may stem from factors such as high intratumoral heterogeneity and the failure of biomarkers to significantly contribute to prognosis based solely on clinical characteristics. Recent studies have revealed the potential of Peritumoral tissue (PTT) as a promising source of prognostic biomarkers. PTT offers complementary information and, in some cases, surpasses the prognostic capacity of tumor tissue-based biomarkers (Huang et al., SciRep 2016; Oh & Lee, Cancer Medicine 2023; Kim et al., Journal of Translational Medicine 2023).
To enhance our understanding of the predictive capacity of peritumoral tissues in clear cell renal cell carcinoma (ccRCC) and discover novel prognostic biomarkers, we applied a systematic approach in order to investigate predictive biomarkers in peritumoral tissue. This process involved re-analyzing molecular data from multiple patient cohorts and various OMIC technologies. Our findings indicate that prognostic models based on PTT exhibit greater transferability between different patient cohorts, and result in more precise survival-prediction and complement models built solely on tumor tissue data. Moreover, we generated a single cell atlas of PTT, carefully merging various public datasets. This new improved single cell dataset further helped the deconvolution of bulk transcriptomes to identify the proportion of cell types to propose a hypothesis for aggressive ccRCC cancers.



### Placental DNAm changes mediating the association between prenatal air pollution exposure and child lung function: a study in the SEPAGES cohort


*by Broséus Lucile, Inserm*

Introduction: Prenatal air pollution exposure (PAPE) may impair respiratory health and reduce lung function in the offspring, notably by triggering oxidative stress and lung inflammation. These effects could be partly mediated by air pollution-induced epigenetic alterations of the placenta. We aimed to investigate the potential mediating role of placental DNA methylation (DNAm) in the effects of prenatal NO2, PM10, PM2.5 and PM2.5 oxidative potential exposure levels on child lung function. 
Methods: Placental DNAm levels were measured using the Infinium Methylation EPIC BeadChip in 395 participants from the French couple-child cohort SEPAGES. PAPE was estimated based on maternal residential address using both personal captors and an ambient dispersion model. Lung function (6 parameters overall) was assessed through tidal breathing analysis and nitrogen multiple breath washout test at two months of age. We conducted adjusted epigenome-wide mediation analyses using the HDMAX2 method to identify genomic loci (CpGs) explaining the association between PAPE and child lung function (FDR<0.2). 
Results: Negative (adverse) total effect (p-value<0.05) were found between PAPE and the functional residual capacity (FRC), an indicator of lung volume. We identified 33 CpGs significantly mediating the association between at least one air pollutant and one lung function parameter in newborns. These included 14 CpGs significantly mediating the association between at least one air pollutant and the FRC, notably sites mapping to the gene MEIS1, involved in lung development and to several genes related to the metabolism and to the immune function.
Discussion: Our findings highlight placental epigenetic biomarkers which might mediate the effect of PAPE on children’s lung function. These results could give clues about the epigenetic modifications through which PAPE affects early and later-life lung function.


###  Guilt-by-association (GBA) centrality - an interactome-based analysis method for disease gene prioritization


*by Kubica Jędrzej, 1) Univ. Grenoble Alpes, CNRS, UMR 5525, TIMC / MAGe, 38000 Grenoble, France; 2) Laboratory of Functional and Structural Genomics, Centre of New Technologies, University of Warsaw, 02-097 Warsaw, Poland*

In network biology, the protein-protein interaction network (interactome) is an essential source of information for identifying biomolecules that underlie diseases and complex phenotypic traits. Indeed, it can be leveraged via the guilt-by-association (GBA) paradigm, which asserts that interacting proteins are more likely to take part in the same biological processes or pathways. Currently, bioinformatics methods that combine a topological analysis of the human interactome with prior knowledge about disease-specific genes and proteins are needed.

Here we present Guilt-by-association (GBA) centrality - a network-based algorithm for disease gene prioritization based on the GBA paradigm. GBA centrality combines the topology of the whole network with prior knowledge about genes that are known to be causal for a particular phenotype. To study the performance of GBA centrality, we constructed a high-quality human interactome using public protein-protein interaction data and we focused on six diverse diseases: two male infertility phenotypes, two cardiopathies and two types of cancer. For each disease, we performed a leave-one-out cross-validation and examined the tissue enrichment of the highest-scoring genes. These analyses show that GBA centrality helps researchers prioritize new promising candidate disease genes in diverse pathologies.


### Benchmark of microRNA targets prediction algorithms using microRNA-mRNA co-sequencing datasets at the single-cell level


*by Velut Louise, Laboratoire BioSanté (CEA)*

Authors: Louise Velut, Laure Fancello, Nadia Cherradi, Laurent Guyon
Abstract: 
MicroRNAs (miRNAs) are small non-coding RNAs that play pivotal roles in the post-transcriptional regulation of gene expression, influencing a wide range of physiological and pathological processes. 
To fully appreciate the regulatory impact of miRNAs, significant efforts have been dedicated to identifying their mRNA targets through in silico predictions and experimental validation. Over the years, more than 100 algorithms have been developed to predict miRNA targets, and were typically validated against simulated or experimental data, such as CLIP-seq and CLASH experiments.
Since 2018, several groups have published datasets of co-sequencing of microRNA and mRNA at the single-cell level. This type of dataset is exceptionally valuable for gaining a deeper understanding of how microRNAs impact the expression of their mRNA targets.
Utilizing these highly informative datasets, we benchmarked seven of the most widely used microRNA target prediction algorithms. Our analysis was based on the expected statistical enrichment of anti-correlations between miRNAs and their mRNA targets. We evaluated the performance of individual algorithms and their combined predictions. We also focused on scores predicted by the algorithms for each target and worked with different numbers of predicted targets. Our findings demonstrate strong performance for TargetScan, Diana-microT-CDS, miRmap, miRDB, and mirDIP, while miRWalk exhibited poorer performance.


### Prediction of proteins belonging to a gene family involved in bacterial secretion systems using machine learning approaches.


*by Sandy Frank KWAMOU NGAHA, TIMC-TrEE*

Proteins are biological molecules made of amino acids that group into hundreds of thousands of different families, involved in functions ranging from structural to chemical roles. They often partner up to fulfil cellular functions and assemble into macro-molecular systems. An example of such macromolecular systems are secretion systems. These protein complexes play vital roles in prokaryotic organisms (bacteria and archaea) as they are used by the organism to interact with their environment for nutrient acquisition, defense, and toxin delivery. While current knowledge identifies 12 types of these systems in bacteria harbouring both an inner and outer membrane (diderm bacteria), evidence suggests the existence of additional ones. Considering the significance of secretion systems in environmental and inter-organism interactions, coupled with the formidable challenge of uncovering new systems (the last discovery took 12 years of experimental research), it is probable that entire categories of secretion systems remain undiscovered.  Current methods for assessing a system's distribution use comparative approaches, analyzing protein sequences similarity and genomic organization. However, since proteins with different sequences can perform the same function, sequence comparison has limitations. Machine learning offers solutions to overcome these challenges and this is the approach we adopted. 
In order to develop machine learning models, we constructed our data from the ncbi database. We downloaded genomes, we deduplicated their proteins through a clustering step using mmseq2, and we created labels by mapping proteins associated to a known secretion system as true. Relevant features were extracted from the sequences. 
After extracting these features, we implemented a cross-validation strategy by creating 5 sets of phylogenetically distant organisms in which we hide particular systems, in order to approach the difficulties and conditions of the final learning task and help evaluate the performance of our developed models. We employed various bagging PU-learning models ( a technique that aggregates multiple models to improve predictive performance and robustness) in both inductive and transductive modes. Our analysis reveals that bagging models based on decision trees classifier and logistic regression outperform traditional positive-negative learning models, demonstrating superior performance in our classification tasks. We validated our best model on an independent validation dataset and we could attend very good performance in terms of identifying new positive proteins. 



### Unwelcome guests: characterizing the ecology and evolution of insertion sequences in prokaryotic genomes

*by GAUDILLIERE Flora, Université Grenoble Alpes*

Insertion sequences (IS) are the simplest kind of autonomous transposable elements found in prokaryotic genomes: they only carry genes encoding proteins responsible for their transposition within genomes. The movement of IS elements can have drastic and often deleterious effects on genetic information and expression; which is why IS elements are mostly considered as parasites in their genomic ecosystems. It is therefore interesting to tackle IS biology using an ecological framework to help formulate relevant questions about IS evolutionary dynamics. In this framework, mobile genetic elements such as IS are considered as organisms that interact and compete for ecological niches available in bacterial genomes.
In our work, we used this genome ecology approach to explore questions related to IS distributions across prokaryotic genomes. For instance, what factors determine which ecosystems (genomes) can be invaded by a given IS? What determines the ecological niche of an IS within a genome? We took advantage of existing automated tools for IS detection to characterize their distributions across 30,482 complete and publicly available prokaryotic genomes. We show that IS distributions are phylogenetically structured, and that this structuration is likely due to barriers to IS transfer between clades. We also highlight the large diversity of IS elements that coexist in most prokaryotic genomes. Using modelling, we identify purifying selection as a major force excluding IS elements from a large part of the genome, which results in their segregation in AT-rich regions, alongside other MGE such as phages. Finally, our analysis suggests that the niches of different IS elements do not entirely overlap: each IS family has a specific niche, which may explain their coexistence within genomes.




### HDMAX2, an R package to perform high dimension mediation analysis


*by PIttion Florence, TIMC CNRS*

"HDMAX2, an R package to perform high dimension mediation analysis"
F. Pittion, B. Jumentier, A. Nakamura, A. Leclercq-Samson, N. Varoquaux, J. Lepeule,
O. François and M. Richard

Abstract:
Mediation analysis plays a crucial role in epidemiology, unraveling the intricate pathways through which exposures exert influence on health outcomes [1]. Recent advances in high-throughput sequencing techniques have generated growing interest in applying mediation analysis to explore the causal relationships between patient environmental exposure, molecular features (such as omics data) and various health outcomes. Mediation analysis handling high-dimensional mediators raise a number of statistical challenges [2]. Despite the emergence of numerous methods designed to tackle these challenges, the majority are limited to continuous outcomes. Furthermore, these advanced statistical approaches have yet to find widespread adoption among epidemiologists and health data scientists in their day-to-day practices. To address this gap, we introduce an R package specifically tailored for high-dimensional mediation analysis, leveraging the HDMAX2 method [3].

Here we improve the HDMAX2 method, and expand its capabilities to accommodate multivariate exposure and non-continuous outcomes. This improvement enables the method’s adaptation to a diverse array of mediation analysis scenarios, mirroring the complexity often encountered in healthcare data. To enhance accessibility for users with varying expertise, we release an R package called hdmax2. This package allows users to estimate the indirect effects of mediators, calculate the overall indirect effect of mediators, and facilitates the execution of high-dimensional mediation analysis. 

Additionally, we extend HDMAX2 to accommodate survival outcomes in high-dimensional mediation analysis. Through comprehensive simulation studies, we demonstrate the validity and performance of this novel extension, although this feature is not yet included in the public release. Our work provides epidemiologists and health data scientists with a robust, versatile tool for investigating complex causal relationships in modern healthcare data.High-Dimension Mediation Analysis.

References
[1] R. M. Baron and D. A. Kenny. The moderator-mediator variable distinction in social psychological research: conceptual, strategic, and statistical considerations. Journal of Personality and Social Psychology, 51(6):1173–1182, December 1986.
[2] Dylan Clark-Boucher, Xiang Zhou, Jiacong Du, et al. Methods for Mediation Analysis with High-Dimensional DNA Methylation Data: Possible Choices and Comparison. medRxiv, page 2023.02.10.23285764, February 2023.
[3] Basile Jumentier, Claire-Cécile Barrot, Maxime Estavoyer, et al. High-dimensional mediation analysis: A new method applied to maternal smoking, placental dna methylation, and birth outcomes. Environmenta Health Perspectives, 131(4):047011, 2023.


### Navigating Variable Selection and Mixture Identification: A Comprehensive Simulation Study with Mixture Models


*by Jovanovic Nicolas, IAB*

Introduction: Mixture models have gained traction in epidemiological research, chiefly for their capacity to evaluate the joint effect of multiple chemicals and identify the primary drivers of this mixture effects. Despite their growing use, guidelines for model selection remain absent. To bridge this gap, relying on simulated data we undertook a comprehensive evaluation of the most widely used mixture models including Bayesian Kernel Machine Regression (BKMR), Bayesian Weighted Quantile Sum (BWQS), and G-computation (GCOMP) models across various scenarios. 

Methods: We simulated 46 realistic exposure variables using an existing correlation matrix from environmental chemicals measured in the blood and urine of European pregnant women. A continuous health outcome was also simulated.

The percentage of exposures truly associated with this outcome varied per scenario (0%, 10% and 20%). The structure of the correlation matrix was also modified to mimic low and highly correlated exposures. 

For each scenario, we generated 100 unique datasets with 500 individuals each and applied the models (BKMR, BWQS, GCOMP, and EWAS (corrected or not for false discovery rate) to each.  

We evaluated models’ ability to identify mixture effect (all models but EWAS), and key drivers of the mixture effect based on sensitivity, false selection rate, F1-statistic.

Results: Regarding mixture detection rate, GQComp detected a significant mixture effects 75% of the time, compared to 33% and 11% for BKMR and BWQS respectively. The ranking was inversed in the high correlation scenario, with BWQS having 97% mixture detection rate, followed by BKMR with 78% and QGComp with 37%. False discovery for mixture effect was low whatever the models and correlation matrix tested (< 10%). 

Regarding identification of individual true exposure, in scenario with low correlation across expo the FDR corrected ExWAS was the model with the highest sensitivity (68%) and lowest (FDR) of 23%. In the high correlation scenario, a high FDR was observed for most models (> 75%%) but BKMR (FDR between 42% and 65%), however for this former model’s sensitivity was also low. 

Discussion: Our simulation results indicated that the choice of model for mixture identification depends on the correlation structure among the exposures considered. In scenarios with moderate or low correlation, QGCOMP emerged as the preferred model. Conversely, in situations of high correlation, BWQS performed better.
For individual chemical identification, none of the mixture models outperformed the classical EWAS approach. Under conditions of high correlation, all models exhibited either a high (FDR) and/or low sensitivity (e.g., BKMR), emphasizing the necessity of shifting paradigms from agnostic to hypothesis-driven approaches.




### The study of quinone exchanges in the gut microbiota


*by Roger-Margueritat Morgane, PhD student - TIMC lab (UGA)*

The gut microbiota integrity is directly correlated to the host’s health (Daisley et al., 2021) and a way to maintain the diversity on its community is to promote the exchange of compounds between donor and recipient bacteria, this phenomenon called cross-feeding (Seth and Taga, 2014). By this way, the discovery of new exchanges could be really useful to keep us healthy. Moreover, the potential exchange of quinones, key molecules in the respiratory chains in the whole tree of life, have been suggested but never characterized (Franza and Gaudu, 2022).
First, the bioinformatic annotation with HMM profiles of the menaquinone (MK) synthesis pathway, the predominant quinone in bacteria (Bentley and Meganathan, 1982), has been performed on the UHGG dataset (Almeida et al., 2021). This reveals several cases of partial MK pathways where the remaining proteins match with the possibility of precursors exchanges in the medium. Furthermore, phylogenetic analyses have been undertaken to study the transmission of the pathway and pointed to the loss of a part of the pathway instead of the horizontal transfer to gain this truncated pathway. To go further, experimental validations have been realized, validating partial MK pathway functionality and the use of precursors provided by other bacteria, and even by the host, has been confirmed in co-cultures. Finally, the whole quinone content in feces reveal a wide range of quinones and this new method is promising to confirm the quinone cross-feeding in vivo, this exchange may one day contribute to impact the dynamics of the gut microbiota.

### Predicting compensatory mutations in proteins using statistical models


*by CHAUVEAU Marion, TIMC Tree, ESPCI Paris Gulliver*

A powerful approach to study protein sequences is through statistical inference. Direct Coupling Analysis (DCA) models, for instance, are designed to capture the statistical behavior of amino acid conservation and correlations within protein families. These approaches have been successfully applied to various tasks, including predicting short-range intra- and inter-protein contacts and designing functional proteins. In this work, we explore how these models' capacity to assess mutational effects can be applied to predict compensatory mutations. As a case study, we investigate the enzyme Dihydrofolate reductase, focusing on a well-documented mutation known to suppress its catalytic activity and we identify a compensatory mutation capable of restoring the enzyme's function.




## Poster

### Does Metabolite Toxicity Impact Gene Order in Metabolic Operons through Selection for Robust Gene Expression? 

*quentin fernandez de grado (TIMC, MAGe)*


Bacterial genomes are organized in operons, grouping multiple genes that are expressed in similar biological conditions. We study the order of genes within operons, a question that has received little attention. The specific question we ask is whether two genes catalyzing two successive reactions of a metabolic pathway are encoded in the same order within their operon than they appear within the pathway. A pioneer study has shown 15 years ago that the answer is yes for more than half of such gene pairs, and suggested a mechanism leading to a selection pressure for coding genes in this order. On the opposite, in this work we are looking for selection pressures which could explain why a significant amount of gene pairs are encoded in the invert genetic order.

For all metabolic operons of E. coli, we computed several features which could directly or indirectly reflect the benefit of the invert genetic order, such as essentiality of each gene, fitness defect associated with knockout or over-expression of each gene, average expression level of the operon, potential toxicity of the intermediate metabolite between the two reactions, and conservation of the genes in their order in other organisms.

We found that fitness defect caused by knockout of the downstream gene within the pathway is significantly associated with the inverse gene order (in which this downstream gene is encoded first in the operon), suggesting that this inverse order arises from a selection pressure for strong and robust expression of the downstream gene. We postulate that in some pathways, this selection pressure could be caused by the toxicity of the intermediate metabolite, leading to a benefit in stronger and more robust expression of the gene which consumes the metabolite than the gene which produces it.

### deconvPDAC: a single-cell based quantifier of PDAC tumor cellular heterogeneity 

*Lucie Lamothe (TIMC, MAGe)*


Abstract

Pancreatic ductal adenocarcinoma (PDAC) is a highly aggressive and invasive tumoral lesion affecting the pancreas. Molecular analysis and classification based on gene expression landscapes iscomplicated by the intrinsic heterogeneity of PDAC tumors. Like all solid cancer, PDAC are madeup of the ‘tumoral mass’ (predominantly epithelial cells) which is surrounded by a microenvironmentcomposed of stromal (fibroblasts, pericytes, endothelial) and immune cells, giving support, nutrientsand sometimes resistance/metastatic potential to neoplastic cells. Precise quantification of this tumorheterogeneity is of utmost importance, as these multiple components are key factors in explainingtumor progression and response to therapy.

A promising approach to accurately quantify cell type heterogeneity in PDAC relies on the recentemergence of bulk deconvolution algorithms based on single-cell reference profiles [1]. One of the mainlimitations of these approaches is the accuracy of the single-cell based profiles, which can stronglyimpair the quantification and the biological interpretation of the inferred tumor composition [2]. Toovercome these difficulties, we built an integrative set of PDAC cell-type specific gene markers, based ona dedicated pre-established gene markers curation and subsequent analysis of PDAC recent single-cellRNA-seq datasets. After several steps of quality control, filtration, annotation and data integration,we launched a systemic identification of integrative cell-types specific gene markers. We then intendto use these markers to revise our current understanding of cell-type heterogeneity in PDAC usingsingle-cell based bulk deconvolution approaches. We also have a goal to build an R package dedicatedto the deconvolution of PDACs, leveraging the robust cell-type specific gene markers and integratedreferences we have been able to establish over the last few years.

References

[1] Francisco Avila Cobos, Mohammad Javad Najaf Panah, Jessica Epps, et al. Effective methods for bulkRNA-seq deconvolution using scnRNA-seq transcriptomes. Genome Biology, 24(1):177, August 2023.

[2] Geng Chen, Baitang Ning, and Tieliu Shi. Single-Cell RNA-Seq Technologies and Related ComputationalData Analysis. Frontiers in Genetics, 10, 2019. Publisher: Frontiers


### Investigating the evolution of phototrophy in Pseudomonadota 

*Timothée SALZAT-HERVOUETTE (TIMC, TrEE)*


Phototrophy is an ancient bacterial metabolism that likely originated over 3 billion years ago, prior to the rise of atmospheric oxygen provoked by oxygenic photosynthesis of Cyanobacteriia. Phototrophy consists in the use of light for cellular energy production. This energy metabolism confers significant adaptive advantages to bacterial species in certain environments, yet it is sparsely distributed across several lineages of the bacterial tree of life. In the phylum Pseudomonadota (formerly Proteobacteria, also referred to as ‘purple bacteria'), phototrophy is also sparsely distributed across various clades, yet it was proposed in the 1980s by Carl Woese that the ancestor of Pseudomonadota was a phototroph. Thus the question of the evolutionary origins and transmission of phototrophy across Pseudomonadota still stands. The genetic potential for phototrophy is encoded by the photosynthetic gene cluster (PGC), a set of ~40 genes that colocalize in the genome and that gathers the genes required to produce photosynthetic pigments, as well as the reaction centers that are part of the light-harvesting antennae. Previous work by others found that the PGC could be found on plasmids, and a recent study suggested that the spread of phototrophy across the family Rhodobacteraceae was facilitated by horizontal gene transfer (HGT) of plasmids containing the PGC. The goal of the present study is to determine the respective contribution of vertical and lateral transmission of phototrophy in Pseudomonadota.To this end, an annotation tool based on the MacSyFinder program was designed for the annotation of PGC in bacterial genomes. More than 250 PGC were detected in 19 777 complete genomes of Pseudomonadota, which enabled subsequent phylogenomic analyses: genome context analyses and phylogenetic reconciliations between the PGC tree and the species tree. Overall, this study investigates the evolutionary history of phototrophy in Pseudomonadota and sets the grounds for a comparative genomic approach to investigate the metabolic factors underlying the sparse distribution of phototrophy across Pseudomonadota.

### Systematic studies on inverted repeat 

*Victor Banon Garcia, (TIMC, TrEE)*



Inverted repeats (IRs), together with directed repeats, tandem repeats, and others, form the basic genetic repetition family that can be found in the primary structure of DNA. An IR is defined as a sequence comprising a pattern (a string composed of characters in ACGT), followed by a gap, and concluded by the reverse complement of the initial pattern. An IR with no gap is a palindrome.

IRs are prevalent in prokaryotic genomes and play crucial roles in various biological processes. They can form hairpin structures (stem-loops) by connecting the two reverse complementary sequences, known as the arms of the structure. IRs are also found in CRISPR-Cas systems, transcription termination and factors, bindings sites of proteins and as restriction sites. Multiple studies have shown they are often abundant in prokaryote's genome while the causes have not yet been thoroughly explained. 

Inspired by previous analyses conducted in eukaryotes and prokaryotes we develop a series of pipelines to efficiently extract and analyze the presence of these patterns. Through systematic studies applied to large datasets of prokaryotes, such as those available in the NCBI, we aim to gain deeper insights into the phylogenetic and genomic distributions of these patterns.

We applied our framework to prokaryotic genomes, and, by estimating the expected number of IRs through permutation of the original sequence and comparing it to the observed sequence using hypothesis testing, we were able to detect interesting patterns. 

As a result, we were able to highlight not only tendencies in the abundance and depletion of IRs that are specific to certain clades but also systematic trends that hold across the bacterial kingdom. Namely, we observed an overall overabundance of IRs, with strong deviations from null models for sizes above X. More precisely, we observed systematic enrichment in IRs of gap length between typically 4 and 6 and arm length larger than ∼8, probably reflecting the selection of functional secondary structures of DNA and RNA in the genomes. We also observed that palindromic sequences are often significantly depleted, consistent with previous works and a scenario of counter-selection imposed by restriction-modification systems.

### Interaction between tumour heterogeneity and cancer evolution 

*Juliette Louistisserand (TIMC, MAGe)*


Pancreatic ductal adenocarcinoma (PDAC) is one of the most aggressive cancers with a particularly poor prognosis. With a 5-year relative survival rate around 11\%, PDAC is predicted to become the third leading cause of cancer-related death in Europe by 2025 and the second in the United States by 2040. 
PDAC tumours are characterised by high heterogeneity, cell plasticity, and poor treatment efficacy. Our project aims to decipher the complex interplay between tumour heterogeneity and cancer evolution in PDAC. 
Firstly, we will apply computational deconvolution methods on bulk data to quantify the heterogeneity of PDAC samples (from public and private dataset). 
In parallel, variant-calling methods will be used to assess the mutational landscape of these samples. The relationship between tumour heterogeneity and mutational profiles will be investigated using canonical discriminant analysis on phenotypic data, potentially revealing specific heterogeneity signatures associated with distinct mutational patterns. 
Finally, given the existence of spatial heterogeneity in tumours, spatial data will be integrated in our analysis to investigate whether the spatial distribution of cancer subclones can be explained by the relationship between mutational profiles and tumor heterogeneity. 
This project will help to have a better understanding of the impact of the tumour heterogeneity on the evolution of cancer cells in PDAC.

### Detection of exact sequence variants in metabarcoding by PCR abundance signal clustering. 

*Alexandre Wendling (LJK)*


Advances over the past decade in high-throughput sequencing (HTS) technologies have significantly enhanced the use of molecular methods for species identification via environmental DNA (eDNA). Metabarcoding—a technique that enables the simultaneous tagging, sequencing, and identification of multiple species from a single environmental sample (Taberlet, Coissac, Hajibabaei, & Rieseberg, 2012)—has become a cornerstone of biodiversity research (Compson et al., 2020). This approach relies on PCR amplification of taxonomically informative genetic fragments ('DNA barcodes'), which are sequenced and matched to reference datasets for species identification. However, the analysis of eDNA faces several challenges, the most important of which is the deterministic amplification bias during PCR (Gold et al., 2023). To improve the accuracy and efficiency of taxonomic assignments in eDNA metabarcoding there is a pressing need for advanced tools that can better differentiate genuine environmental signals from the noise inherent in molecular detection processes (Mathon et al., 2021). PCR amplification biases often result in amplicon sequence variants (ASVs) (Callahan, 2017), which do not correspond to real sequences, as has been observed in mock community studies. Currently, the classical way to filter out these spurious sequences is by comparing them with reference databases. However, databases are often much incomplete at least for certain taxonomies, and setting the right similarity threshold can be cumbersome in practice. To improve biodiversity descriptions from eDNA, we propose an alternative approach: leveraging the variability in the abundance of sequences across samples and PCR replicates to delineate between true and spurious ASVs without relying on reference databases. This requires adaptation to metabarcoding data of well-established methods in compositional abundance clustering such as SparCC (Friedman & Alm, 2012) or PNL model (Aitchison & Ho, 1989). In an ongoing work, we aim to evaluate these statistical methods on mock and real communities. In further studies, we will develop machine learning models coping with unmodeled noise, and allowing to create vector space representation of amplicon data.

### A robust and reproducible workflow to benchmark cell type deconvolution of -omic data 

*Elise Amblard (TIMC, MAGe)*


Tumour heterogeneity significantly affects cancer progression and therapeutic response, yet quantifying it from bulk molecular data remains challenging. Deconvolution algorithms, which estimate cell-type proportions in bulk samples, offer a potential solution. However, there is no consensus on the optimal algorithm for transcriptomic or methylomic data.

Here, we present an unbiased evaluation framework for the first comprehensive comparison of deconvolution algorithms across both omic types, including reference-based and -free approaches. Our evaluation covers raw performance, stability, and computational efficiency under varying conditions, such as missing or additional cell types and diverse sample compositions. We apply this framework across multiple benchmark datasets, including a novel multi-omics dataset generated specifically for this study. To ensure transparency and re-usability, we have designed a reproducible workflow using containerization and publicly available code.

Our results highlight the strengths and limitations of various algorithms, and provides practical guidance for selecting the best method based on data type and analysis context. This benchmark sets a new standard for evaluating deconvolution methods and analysing tumour heterogeneity.

### Machine learning based alignment of mass spectrometry data for improved clinical biomarker discovery  

*Alicia Lionneton, (EDyp)*



Chromatography coupled with Mass-spectrometry (LC-MS) is a reference method to characterize proteins at scale in biological samples. However, this approach still lacks exhaustiveness as some proteins may not be screened for various chemical reasons. To cope with this, it is common practice to pool identifications from several similar samples in order to transfer identifications to samples in which they may be missing. Notwithstanding, owing to the lack of reproducibility of different LC-MS runs, it can also generate some errors. Therefore, this study focuses on two challenges: first improve the identification transfer itself (referred to as match-between-run or MBR in the proteomic parlance), and second, control the associated error rate.

In LC-MS based proteomics, proteins are digested by an enzyme into peptides that are separated by LC before being screened with MS. The MS iterates two steps : First, an MS1 spectrum summarizing all peptides’ mass-to-charge (m/z) ratio is recorded, in which some peptides are selected for subsequent fragmentation (those left behind are the reason for the lack of exhaustiveness of the approach). Second, several MS2 spectra are generated (one for each fragmented peptide). MS2 spectra are used to determine the amino acid sequence of a peptide, and thus to identify its mother proteins in the reference databases. To overcome the lack of exhaustiveness, MBR allows transferring a peptide identification from one run to another run based on some characteristics such as retention times (RT) and m/z.

Because LC is not fully reproducible, the peptide RT may vary from one sample to another. To avoid this variability leads to errors when transferring identification from one run to another, RTs must be aligned beforehand. Among other alignment techniques, the Loess regression is the most commonly used. However, it suffers some drawbacks such as ignoring some proteins’ properties or providing only a point estimate of RTs without a confidence interval. We suggest improving the alignment procedure by using kernel regression endowed with a confidence interval.

Beside improving MBR, it is important to correctly estimate the risk of incorrect identification transfer, which could lead to spurious biological conclusions. To assess this overlooked issue, we propose to build a metric, based on cross-validation.

Future work will focus on assessing, polishing and implementing the mentioned improvements  in an internal software application.

### Wnt/β-catenin pathway activation in ACC tumors using pathway somatic alterations or expression of the LEF1 downstream effector 

*Laura Fancello (IRIG)*


Adrenocortical carcinoma (ACC) is a rare and aggressive cancer of the adrenal cortex. Aberrant activation of the Wnt/β-catenin signaling is observed in nearly 40% of ACC cases and is associated to poor prognosis. Indeed, activating mutations in CTNNB1 gene, encoding for β-catenin, are one of the most frequent genetic alterations in ACC (Assié et al. Nat genet 2014; Zheng at al. Cancer Cell 2016). These mutations lead to β-catenin stabilization and nuclear import with subsequent constitutive activation of the T-cell factor/lymphoid enhancer factor (TCF/LEF)-dependent transcription of β-catenin target genes. Other somatic mutations, i.e. inactivating mutations of the negative regulators of the Wnt/β-catenin signaling ZNRF3 and APC, are known to cause aberrant activation of the Wnt/β-catenin signaling in ACC. Nonetheless, several tumors present β-catenin activation in the absence of known mutations. Therefore, somatic alterations are not optimal to identify ACC tumors with Wnt/β-catenin signaling activation. In diagnostics, immunostaining of the β-catenin protein, which is normally membranous but translocates to the nucleus over activation of the Wnt/β-catenin signaling, is widely used. However, quantification of its nuclear versus membranous localization can be hard to determine.
We recently observed that the mRNA expression of LEF1, a member of the TCF/LEF transcriptional complex that is also a canonical transcriptional target of the Wnt/β-catenin signaling, is associated with survival in two public ACC patient cohorts, with better statistical power than the mutational status of the Wnt/β-catenin pathway (Cristante et al. bioRxiv 2023). Interestingly, LEF1 immunostaining was recently proposed instead of β-catenin nuclear versus membranous immunostaining, because of its easier readout (Hewer et al. J Clin Pathol 2024).
In this work, we further investigate the potential of LEF1 gene expression as a surrogate marker of β-catenin activation, extending our analysis and using two additional transcriptomic datasets. When comparing tumors with high versus low LEF1 expression, we observed a positive enrichment in Wnt/β-catenin pathway and an enrichment in LEF1 transcription factor binding site motifs among genes upregulated in LEF1 high condition, which supports our hypothesis. We then characterized the transcriptional changes associated with Wnt/β-catenin pathway activation across several cohorts of patients. We could define a small subset of β-catenin targets most consistently upregulated across the cohorts, to be further tested as a gene signature of Wnt/β-catenin pathway activation. Finally, we identified across all patient cohorts consistent changes in association with β-catenin activation, related to immune response, cell cycle and extracellular vesicles biogenesis related-genes, the latter supporting some original observations in the ACC cell line H295R from recent experiments in our laboratory.

### Unraveling UbiO: a newly characterized enzyme of the ubiquinone biosynthesis pathway


*by BOUVET Emma, TIMC TrEE*

Ubiquinone (UQ, “coenzyme Q” in eukaryotes), shuttles electrons within electron transfer chains, and as such plays an essential role across a broad range of organisms. Despite the overall conservation of its biosynthetic pathway, recent findings suggest significant diversification in the hydroxylation and decarboxylation steps across the bacterial phylum of Pseudomonadota (ex-Proteobacteria). The recent discovery of UbiO, an enzyme found in Rhodobacter capsulatus that is capable of both decarboxylation and hydroxylation led us to investigate whether it was present in other Pseudomonadota. By combining heterologous expression of candidate genes in Escherichia coli and phylogenomic approaches, we attempt to delineate the UbiO protein family within the widespread and large flavin monooxygenase family. Our first results extend the UbiO protein to the entire family of Rhodobacterales. Thus, by integrating phylogenetic reconstructions with in vivo experimental validation, this study highlights how essential metabolic pathways can diversify in the constrained frame of a biosynthesis pathway with a conserved precursor and a conserved final product. Overall, the investigation of the UQ biosynthetic pathway contributes to a deeper understanding of enzymatic and biosynthetic pathways’ evolution.

