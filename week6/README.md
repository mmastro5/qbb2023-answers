1.1 plink command

plink --noweb --vcf genotypes.vcf --pca 10


2.1 plink command
plink --vcf genotypes.vcf --make-bed --out genotypes_plink
plink --bfile genotypes_plink --freq --out allele_frequencies

3.1 plink command
plink --vcf genotypes.vcf --linear --pheno GS451_IC50.txt --covar plink.eigenvec --allow-no-sex --out phenotypeA_gwas_results
AND
plink --vcf genotypes.vcf --linear --pheno CB1908_IC50.txt	 --covar plink.eigenvec --allow-no-sex --out phenotypeB_gwas_results


3.4 
* searched the snp postition of each phenotype from my code
GS451_IC50 (rs7257475): Gene ZNF826 - moderately similar to Zinc finger protein 91, if mutated would not work cooperately with the complex it is a part of. 

CB1908_IC50 (rs10876043): Gene DIP2B - The encoded protein contains a binding site for the transcriptional regulator DNA methyltransferase 1 associated protein 1 as well as AMP-binding sites. The presence of these sites suggests that the encoded protein may participate in DNA methylation, so could cause issues with methylation if mutated. 