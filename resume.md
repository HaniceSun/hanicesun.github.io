<!-- The (first) h1 will be used as the <title> of the HTML page -->
# Han Sun, PhD
<!-- The unordered list immediately after the h1 will be formatted on a single
line. It is intended to be used for contact details -->
- <hansun@stanford.com>
- [LinkedIn](https://www.linkedin.com/in/sunhanice/)
- [GitHub](https://github.com/HaniceSun)
- 3165 Porter Drive, Palo Alto, CA 94304

<!-- The paragraph after the h1 and ul and before the first h2 is optional. It
is intended to be used for a short summary. -->

## Experience

<!-- You have to wrap the "left" and "right" half of these headings in spans by
hand -->

### <span>Research Scientist/Senior Computational Biologist</span> <span>2020 -- </span>

Department of Pediatrics, School of Medicine, Stanford University, **[Prof. Anna Gloyn](https://med.stanford.edu/genomics-of-diabetes.html)**

### <span>Postdoc</span> <span>2015 -- 2019</span>

Department of Genetics, School of Medicine, Stanford University, **[Prof. Lars Steinmetz](https://web.stanford.edu/group/steinmetzlab/cgi-bin/wordpress/?page_id=59)**

## Education

### <span>PhD, Bioinformatics</span> <span>2009 -- 2014</span>

Key Lab of Systems Biology, Shanghai Institutes for Biological Sciences, 

University of Chinese Academy of Sciences, **Prof. Yixue Li** and **Prof. Lu Xie**

### <span>Bachelor, Software Engineering</span> <span>2004 -- 2008</span>

East China Normal University

## Projects

- **Splicing-mediated oncogene activation in multiple cancers**

By reanalyzing both whole exome sequencing and RNA-Seq data of over 10,000 patients across 33 cancer types from the TCGA project using a generalized linear model, I observed a very interesting correlation between somatic mutations, splicing between the adjacent genes, and the overexpression of the downstream gene in subsets of cohorts, including the top hit, mutation within CDKN1A, splicing between CDKN1A and RAB44, and the activation of RAB44 in bladder, stomach, and skin cancer. I established the causality through collaboration with other labs by introducing the mutation in cell lines using CRISPR/Cas9. We further performed functional/phenotyping assays to illustrate the connection from RAB44 activation to MDM2 upregulation and TP53 downregulation. I proposed a splicing-mediated readthrough stabilization (SRS) model as one more mechanism for oncogene activation to explain this type of atypical transcript fusion events instead of the common gene fusions on the genomic level.

- **RNA-binding protein RBM20-deficient dilated cardiomyopathy**

Starting from a family with dilated cardiomyopathy, I analyzed whole exome sequencing (WES) and whole genome sequencing (WGS) data from the family members and identified a suspicious missense mutation in RBM20 through linkage analysis. Considering RBM20 is an RNA-biding protein, I further identified its splicing targets from human and pig RNA-Seq data. We validated this finding by doing CRISPR/Cas9 editing in human induced pluripotent stem (iPS) cells and differentiating them to cardiomyocytes. By integrating gene expression data from GTEx, I proposed a model about tissue-specific splicing of a mitochondrial inner membrane protein, IMMT, suggesting a molecular connection between deficiency in energy-supplying and dilated cardiomyopathy.

- **Mutation and mechanisms underlying neonatal diabetes**

By analyzing whole genome sequencing and array based genotyping data from mice, I identified a suspicious intronic mutation that correlates with neonatal diabetes. We validated that the mutation is indeed diabetes causing using CRISPR/Cas9 editing. I proposed a mechanism that the mutation leads to a novel splice site resulting in longer isoform but truncated protein which has also been verified. We are working on bulk and single cell data (scRNA-Seq and scATAC-Seq) from along development to investigate additional regulatory elements to explain why the phenotype is pancreas specific.

- **Deep learning prediction of tissue specific splicing**

Starting from reproducing the famous model of SpliceAI using both Tensorflow and Pytorch, I am attempting and evaluating models such as attention with GPT backbone, and fourier transform based global convolution (Hyena), to replace the CNN component in SpliceAI, with an application in long-reads sequencing data (PacBio) from multiple tissues including islets.


## Research Interests

- Disease Genetics (Cancer, Cardiomyopathy, Diabetes, ...)

- Multiomics (bulk and single cell)

- AI 4 Life Sciences (CNN, Transformer, GNN)

## Scientific Skills

- Python, R, C, git, Linux, and High Performance Computing

- statsmodels, scikit-learn, Tensorflow, and PyTorch

- Bioinformatics and Biostatistics

- Machine Learning and Deep Learning

- Genomics, Transcriptomics, Proteomics, and Epigenomics

- Linkage analysis, QTL mapping, and GWAS

## Patents

- Methods of Treatment, Genetic Screening, and Disease Models for Heart Conditions Associated with RBM20 Deficiency. Francesca Briganti, Lars M. Steinmetz, Han Sun, and Wu Wei. WO 2020/092171.

## Publications

1. **Han Sun**, Huiying Yan, Kathryn Bieging-Rolett, Michelle Nguyen, William F. Mueller, Zhuanfen Cheng, Hong Zeng, Laura Attardi, Wu Wei, and Lars M. Steinmetz et al. "CDKN1A-RAB44 transcript fusion and oncogene activation in cancers.", [bioRxiv](https://www.biorxiv.org/content/biorxiv/early/2019/02/22/111856.full.pdf).

1. Francesca Briganti, **Han Sun**, Wu Wei, Jingyan Wu, Chenchen Zhu, Martin Liss, Ioannis Karakikes et al. "iPSC Modeling of RBM20-Deficient DCM Identifies Upregulation of RBM20 as a Therapeutic Strategy." <u>Cell Reports</u> 32, no. 10 (2020): 108117, **co-first author**.

1. Rottner, Antje K., Yingying Ye, Elena Navarro-Guerrero, Varsha Rajesh, Alina Pollner, **Han Sun**, Romina J. Bevacqua, Jing Yang et al. "A genome-wide CRISPR screen identifies CALCOCO2 as a regulator of beta cell function influencing type 2 diabetes risk." <u>Nature Genetics</u> 55, no. 1 (2023): 54-65.

1. Lau, Hwee Hui, Nicole AJ Krentz, Fernando Abaitua, Marta Perez-Alcantara, **Han Sun**, Jun-Wei Chan, Jila Ajeian, Soumita Ghosh et al. "PAX4 loss of function increases diabetes risk by altering human pancreatic endocrine cell development." <u>Nature Communications</u> 14, no. 1 (2023): 6119.

1. Mattis, Katia K., Nicole AJ Krentz, Christoph Metzendorf, Fernando Abaitua, Aliya F. Spigelman, **Han Sun**, Jennifer M. Ikle et al. "Loss of RREB1 in pancreatic beta cells reduces cellular insulin content and affects endocrine cell gene expression." <u>Diabetologia</u> 66, no. 4 (2023): 674-694.

1. Cortez, Briana N., Hui Pan, Samuel Hinthorn, **Han Sun**, Nicola Neretti, Anna L. Gloyn, and Cristina Aguayo-Mazzucato. "Heterogeneity of increased biological age in type 2 diabetes correlates with differential tissue DNA methylation, biological variables, and pharmacological treatments." <u>GeroScience</u> (2023): 1-21.

1. Torres, Jason M., **Han Sun**, Vibe Nylander, Damien J. Downes, Martijn van de Bunt, Mark I. McCarthy, Jim R. Hughes, and Anna L. Gloyn. "Inferring causal genes at type 2 diabetes GWAS loci through chromosome interactions in islet cells." <u>Wellcome Open Research</u> 8 (2023).

1. Alghamdi, Tamadher A., Nicole AJ Krentz, Nancy Smith, Aliya F. Spigelman, Varsha Rajesh, Alokkumar Jha, **Han Sun**, Mourad Ferdaoussi et al. "Zmiz1 is required for mature β-cell function and mass expansion upon high fat feeding." <u>Molecular Metabolism</u> 66 (2022): 101621.

1. Chenchen Zhu, Jingyan Wu, **Han Sun**, Francesca Briganti, Benjamin Meder, Wu Wei, and Lars M. Steinmetz. "Single-molecule, full-length transcript isoform sequencing reveals disease-associated RNA isoforms in cardiomyocytes." <u>Nature Communications</u> 12, no. 1 (2021): 1-9.

1. Benedikt Rauscher, William F Mueller, Sandra Clauder-Münster, Petra Jakob, M Saiful Islam, **Han Sun**, Sonja Ghidelli-Disse, Markus Boesche, Marcus Bantscheff, Hannah Pflaumer, Paul Collier, Bettina Haase, Songjie Chen, Rene Hoffman, Guangwen Wang, Vladimir Benes, Gerard Drewes, Michael Snyder, Lars M Steinmetz. "Patient-derived gene and protein expression signatures of NGLY1 deficiency", <u>Journal of Biochemistry</u>, 2021

1. Semih Calamak, Menekse Ermis, **Han Sun**, Saiful Islam, Michael Sikora, Michelle Nguyen, Vasif Hasirci, Lars M. Steinmetz, and Utkan Demirci. "A Circulating Bioreactor Reprograms Cancer Cells Toward a More Mesenchymal Niche." <u>Advanced Biosystems</u> 4, no. 2 (2020): 1900139, **co-first author**.

1. Jay W Schneider, Saji Oommen, Muhammad Y Qureshi, Sean C Goetsch, Rhianna S Sundsbak, Wei Guo, Mingming Sun, **Han Sun**, Dennis A Webster, Alex W Coutts, Francesca Briganti, Wu Wei, Lars Steinmetz, Daniel F Carlson, and Timothy J. Nelson et al. "Dysregulated ribonucleoprotein granules promote cardiomyopathy in RBM20 gene-edited pigs", <u>Nature Medicine</u> (2020): 1-13.

1. William F. Mueller, Petra Jakob, **Han Sun**, Sandra Clauder-Münster, Sonja Ghidelli-Disse, Diana Ordonez, Markus Boesche, Marcus Bantscheff, Paul Collier, Bettina Haase, Vladimir Benes, Malte Paulsen, Peter Sehr, Joe Lewis, Gerard Drewes, Lars M. Steinmetz. "Loss of N-glycanase 1 Alters Transcriptional and Translational Regulation in K562 Cell Lines." <u>G3: Genes, Genomes, Genetics</u> (2020).

1. Arne H. Smits, Frederik Ziebell, Gerard Joberty Nico Zinn, William F. Mueller, Sandra Clauder-Munster, Paola Grandi, Petra Jakob, Anne-Marie Michon, **Hanice Sun**, Karen Tessmer, Tilmann Burckstummer, Marcus Bantscheff, Lars M. Steinmetz, Gerard Drewes, and Wolfgang Huber. "Biological plasticity rescues target activity in CRISPR knock outs.", <u>Nature Methods</u> 2019 Oct 28:1-7.

1. Suo, Lun, Yu Xiao Zhou, Li Ling Jia, Hai Bo Wu, Jin Zheng, Qi Feng Lyu, Li Hua Sun, **Han Sun**, and Yan Ping Kuang. "Transcriptome profiling of human oocytes experiencing recurrent total fertilization failure." <u>Scientific Reports</u> 8, no. 1 (2018): 17890.

1. **Han Sun**, Chen Chen, Baofeng Lian, Menghuan Zhang, Xiaojing Wang, Bing Zhang, Yixue Li, Pengyuan Yang, and Lu Xie. 2015. "Identification of HPV Integration and Gene Mutation in HeLa Cell Line by Integrated Analysis of RNA-Seq and MS/MS Data." <u>Journal of Proteome Research</u> 14 (4): 1678–86, **co-first author**.

1. **Han Sun**, Chen Chen, Meng Shi, Dandan Wang, Mingwei Liu, Daixi Li, Pengyuan Yang, Yixue Li, and Lu Xie. 2014. "Integration of Mass Spectrometry and RNA-Seq Data to Confirm Human Ab Initio Predicted Genes and lncRNAs." <u>Proteomics</u> 14 (23-24): 2760–68, **co-first author**.

1. **Han Sun**, Xiaobin Xing, Jing Li, Fengli Zhou, Yunqin Chen, Ying He, Wei Li, et al. 2013. "Identification of Gene Fusions from Human Lung Cancer Mass Spectrometry Data." <u>BMC Genomics</u> 14 Suppl 8 (December): S5, **co-first author**.

1. Zhen-Hao Liu, Bao-Feng Lian, Qiong-Zhu Dong, **Han Sun**, Jin-Wang Wei, Yuan-Yuan Sheng, Wei Li, et al. 2018. "Whole-Exome Mutational and Transcriptional Landscapes of Combined Hepatocellular Cholangiocarcinoma and Intrahepatic Cholangiocarcinoma Reveal Molecular Diversity." <u>Biochimica et Biophysica Acta</u> 1864 (6 Pt B): 2360–68.

1. Menghuan Zhang, Hong Li, Ying He, **Han Sun**, Li Xia, Lishun Wang, Bo Sun, et al. 2015. "Construction and Deciphering of Human Phosphorylation-Mediated Signaling Transduction Networks." <u>Journal of Proteome Research</u> 14 (7): 2745–57.

1. Wei Li, Jian Yu, Baofeng Lian, **Han Sun**, Jing Li, Menghuan Zhang, Ling Li, Yixue Li, Qian Liu, and Lu Xie. 2015. "Identifying Prognostic Features by Bottom-up Approach and Correlating to Drug Repositioning." <u>PloS One</u> 10 (3): e0118672.

1. Jing Li, Jia Jia, Hong Li, Jian Yu, **Han Sun**, Ying He, Daqing Lv, et al. 2014. "SysPTM 2.0: An Updated Systematic Resource for Post-Translational Modification." <u>Database: The Journal of Biological Databases and Curation</u> 2014 (April): bau025.

1. Yulin Dai, Shengdi Li, Xiao Dong, **Han Sun**, Chao Li, Zhi Liu, Beili Ying, Guohui Ding, and Yixue Li. 2013. "The de Novo Sequence Origin of Two Long Non-Coding Genes from an Inter-Genic Region." <u>BMC Genomics</u> 14 (Suppl 8): S6.

1. Li Xia, Tong-Dan Wang, Shao-Ming Shen, Meng Zhao, **Han Sun**, Ying He, Lu Xie, et al. 2013. "Phosphoproteomics Study on the Activated PKCδ-Induced Cell Death." <u>Journal of Proteome Research</u> 12 (10): 4280–4301.

1. Jian Yu, Xiaobin Xing, Lingyao Zeng, Jiehuan Sun, Wei Li, **Han Sun**, Ying He, et al. 2012. "SyStemCell: A Database Populated with Multiple Levels of Experimental Data from Stem Cell Differentiation Research." <u>PloS One</u> 7 (7): e35230.

1. Ying He, Menghuan Zhang, Yuanhu Ju, Zhonghao Yu, Daqing Lv, **Han Sun**, Weilan Yuan, et al. 2011. "dbDEPC 2.0: Updated Database of Differentially Expressed Proteins in Human Cancers." <u>Nucleic Acids Research</u> 40 (D1): D964–71.

1. Xiao Chang, Yun Li, Jie Ping, Xiao-Bin Xing, **Han Sun**, Peng Jia, Chuan Wang, Yuan-Yuan Li, and Yi-Xue Li. 2011. "EcoBrowser: A Web-Based Tool for Visualizing Transcriptome Data of Escherichia Coli." <u>BMC Research Notes</u> 4 (October): 405.

1. Xiao-Bin Xing, Qing-Run Li, **Han Sun**, Xing Fu, Fei Zhan, Xiu Huang, Jing Li, et al. 2011. "The Discovery of Novel Protein-Coding Features in Mouse Genome Based on Mass Spectrometry Data." <u>Genomics</u> 98 (5): 343–51.
