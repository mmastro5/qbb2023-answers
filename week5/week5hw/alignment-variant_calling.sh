#!/bin/bash

#EXERCISE 1
## 1.1 
#________________________________________________________
#Did this in the command line to indew the reference genome:
## bwa index sacCer3.fa 


##1.2 
#____________________________________________________________


# for sample in A01_09 A01_11 A01_23 A01_24 A01_27 A01_31 A01_35 A01_39 A01_62 A01_63
# do 
# 	echo " Aligning sample: " $sample
# 	bwa mem -t 4 -R "@RG\tID:${sample}\tSM:${sample}" sacCer3.fa ${sample}.fastq  > ${sample}.sam
# done

##1.3 
#________________________________________________________________________________

# for sample in A01_09 A01_11 A01_23 A01_24 A01_27 A01_31 A01_35 A01_39 A01_62 A01_63
# do 
# 	echo "Sorting/Indexing sample: " $sample
# 	samtools sort ${sample}.sam  > ${sample}.bam
# 	samtools index ${sample}.bam
# done



#EXERCISE 2
## 2.1
#_________________________________________________________________________________
#freebayes -f sacCer3.fa A01_09.bam A01_11.bam A01_23.bam A01_24.bam A01_27.bam A01_31.bam A01_35.bam A01_39.bam A01_62.bam A01_63.bam > yeastA01.vcf

#2.2
#______________________________________________________________________________________________
# vcffilter -f "QUAL > 20" yeastA01.vcf > filtered.yeastA01.vcf

#2.3
#___________________________________________________________________________
# vcfallelicprimitives -k -g filtered.yeastA01.vcf > reduced.filt.yeastA01.vcf

#2.4
#________________________________________________________________________________________________
snpEff ann R64-1-1.105 reduced.filt.yeastA01.vcf > annotated.vcf
