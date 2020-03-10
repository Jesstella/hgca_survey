# hgca_survey
Survey of Hipparcos Gaia Catalog of Accelerations to Assess Binarity.

### Notes for SS20_cross_match_koa_megafile
This code allows the user to cross-match a file with a Gaia RA and Dec to a file downloaded from KOA containing a list of files with observation times. 
- The epoch used to shift the RA and Dec from the Gaia frame to the Keck observations is created by adding the Gaia RA and Dec in quadrature. 
- KOA file lists could come with RA and Dec values listed as 'NaN'. The code will clean these out before running the comparsion, meaning obviously that these observations will not be included in the cross-match. 

### Notes for SS20_code_for_missing_columns
- Incase the user needs another column pulled from the original datafile. This code can be used. Example given is for column 'pmdec_hip'. 

### Notes for SS20_simbad_object_types
- User can designate list of HIP IDs as as list of number, code will format for SIMBAD. 
- The following strings were chosen as object types that represent binary systems in SIMBAD: 

** - Double/Multiple </br>
SB* - Spectroscopic binary </br>
bL* - Eclipsing binary of beta Lyr type </br>
LXB - Low-mass X-ray binary </br>
Al* - Eclipsing binary of Algol type </br>
EB* - Eclipsing binary </br>
\*i\* - Star in double system </br>
WU* - Eclipsing binary of W UMa type </br>

NB: There are more object types in SIMBAD that are indicative of multiple star systems, this code only uses those relevant to our work. 

### Notes for SS20_wds_search
- User can desginate list of HIP IDs as as list of number, code will format for Vizier >> WDS.
- The query sets a radius of 0.1arcsecond search radius. The intent here is to only pull the HIP star, as the WDS catalog will list the counterparts to that star as part of the query. Making the radius to wide may include other systems. 
- NB: Making the radius too small will prevent stars from being returned. 
- The initial search section of the code called the WDS names using HIP ID's. Each of these is pulled from the server in turn so can take a while. Be mindful that if any of the queries were to take longer than 10 seconds (lagging internet etc.) then the code can fail. The list of names will save and the user can adjust the code to continue the list from that spot. 
- The second search is from a downloaded version of the catalog. This runs quicker and will produce the observation dates, position angles and separations for two separate observations of the primary star with one companion. It will also return the magnitude of the primary and secondary star, and the magnitude difference. 

### Notes for SS20_gaia_search 
- At this stage the Gaia search only retrieves how many companions the star has and not the data file, although this will be updated in time. 
- NB: Querying of the targets can take time and the user should be prepared for this. 

### Notes for SS20_accelerations
- Code based on acceleration code written by Elena Mitra.

### Notes for SS20_sigma_calculations
- Code creates sigma values for RA and Dec in both Gaia and Hipparcos. 

### Notes for SS20_interesting_stars
- Code determines which stars are 'interesting' based on the users criteria of how many companions are found in a system and how high the acceleration of the primary star is. Currently assumes 0 binaries and an astrometric acceleration of 100m/s/yr.

### Notes for SS20_compiling_spreadsheet 
- Code will compile all the calculated elements of each system into a spreadsheet with all systems. If the above code has been used, this script should run without complaint.
