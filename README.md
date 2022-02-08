# Models-for-identifying-serotype-1-and-2-among-Riemerella-anatipestifer
## Background
- Models developed for rapid serotyping among RA.
- Two machine learning algorithms (Random Forest and Support Vector Machine) was used for model building.
- The datasets used for model building is composed of mass spectrometry data, containing the intensity and M/Z loci.
- Sample preparation and running the mass spectrometer (Bruker Daltonics, microflex LT):
  * The stored RA isolates were re-cultured 24h 37℃ at carbon dioxide incubator (Memmert, Germany) on Todd Hewitt Broth (DB, USA) blood plate.
  * The single colony was dipped from the plate and smearing the culture onto a spot of the target plate (Bruker Daltonics, Bremen, Germany). Each isolates was imposed with two replicated spots to reduce error.
  * 1μL 70% formic acid (Bruker Daltonics, Bremen, Germany) were added to each spot to extract the bacteria protein.
  * Each spot was covered with 1μL of HCCA matrix (Bruker Daltonics, Bremen, Germany).
  * The machine was run in diagnostic (IVD) mode, and the range of spectra was between 2000-20000 m/z.
## Usage
After setting up the dataset path, run the .py scritpts or run the code line by line in this repository, in python 3.8.
