# Models-for-identifying-serotypes-1-and-2-of-Riemerella-anatipestifer
## Description
- Models developed for rapid serotyping among RA.
- Two machine learning algorithms (Random Forest and Support Vector Machine) were used for models building.
- The datasets used for model building is composed of mass spectrometry data, containing the intensity and M/Z loci.
- Sample preparation and running the mass spectrometer (Bruker Daltonics, microflex LT):
  * The stored RA isolates were re-cultured 24h 37℃ at carbon dioxide incubator (Memmert, Germany) on Todd Hewitt Broth (DB, USA) blood plate.
  * The single colony was dipped from the plate and smearing the culture onto a spot of the target plate (Bruker Daltonics, Bremen, Germany). Each isolates was imposed with two replicated spots to reduce error.
  * 1μL 70% formic acid (Bruker Daltonics, Bremen, Germany) were added to each spot to extract the bacteria protein.
  * Each spot was covered with 1μL of HCCA matrix (Bruker Daltonics, Bremen, Germany).
  * The machine was run in diagnostic (IVD) mode, and the range of spectra was between 2000-20000 m/z.
- Additional file 1
  * Mass spectrometry dataset of Riemerella anatipestifer strains of serotype 1 and other serotypes, this dataset was used to train the classifiers that differentiates serotype 1 from other serotypes among R. anatipestifer.
- Additional file 2
  * Mass spectrometry dataset of Riemerella anatipestifer strains of serotype 2 and the others, this dataset was used to train the classifiers that differentiates serotype 2 from other serotypes among R. anatipestifer.
## Usage
After setting up the dataset path, run the .py scritpts or run the code line by line in this repository, in python 3.8.
