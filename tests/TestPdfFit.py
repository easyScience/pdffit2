#!/usr/bin/env python

"""Unit tests for PdfFit.py
"""

# version
__id__ = '$Id$'

import os
import unittest

# useful variables
thisfile = locals().get('__file__', 'file.py')
tests_dir = os.path.dirname(os.path.abspath(thisfile))
testdata_dir = os.path.join(tests_dir, 'testdata')

from diffpy.pdffit2 import PdfFit
from diffpy.pdffit2 import pdffit2

def testdata(filename):
    """prepend testdata_dir to filename.
    """
    return os.path.join(testdata_dir, filename)

##############################################################################
class TestPdfFit(unittest.TestCase):

    places = 6

    def setUp(self):
        self.P = PdfFit()
        return

    def tearDown(self):
        del self.P
        return

#   def test_intro(self):
#       """check PdfFit.intro()
#       """
#       return

    def test_add_structure(self):
        """check PdfFit.add_structure()
        """
        # skip test when diffpy.Structure is not installed
        try:
            from diffpy.Structure import Structure
        except ImportError:
            return
        ni = Structure(filename=testdata('Ni.stru'))
        self.P.add_structure(ni)
        self.assertEqual(4, self.P.num_atoms())
        return

#   def test_read_struct(self):
#       """check PdfFit.read_struct()
#       """
#       return
#
#   def test_read_struct_string(self):
#       """check PdfFit.read_struct_string()
#       """
#       return
#
#   def test_read_data(self):
#       """check PdfFit.read_data()
#       """
#       return
#
#   def test_read_data_string(self):
#       """check PdfFit.read_data_string()
#       """
#       return
#
#   def test_read_data_lists(self):
#       """check PdfFit.read_data_lists()
#       """
#       return
#
#   def test_pdfrange(self):
#       """check PdfFit.pdfrange()
#       """
#       return
#
#   def test_reset(self):
#       """check PdfFit.reset()
#       """
#       return

    def test_alloc(self):
        """check PdfFit.alloc()
        """
        # alloc and read_struct can be called in any order.
        self.P.alloc('X', 25, 0.0, 0.01, 10, 1000)
        # without a structure calculated PDF is all zero
        self.P.calc()
        Gzero = self.P.getpdf_fit()
        self.assertEqual(1000*[0.0], Gzero)
        self.P.read_struct(testdata('Ni.stru'))
        self.P.calc()
        # check r-values
        rgrid = [0.01*i for i in range(1, 1001)]
        self.assertEqual(rgrid, self.P.getR())
        Gfit_alloc_read = self.P.getpdf_fit()
        # now try the other order
        self.P.reset()
        self.P.read_struct(testdata('Ni.stru'))
        self.P.alloc('X', 25, 0.0, 0.01, 10, 1000)
        self.P.calc()
        Gfit_read_alloc = self.P.getpdf_fit()
        # and they should be the same
        self.assertEqual(Gfit_read_alloc, Gfit_alloc_read)
        return

#   def test_calc(self):
#       """check PdfFit.calc()
#       """
#       return
#
#   def test_refine(self):
#       """check PdfFit.refine()
#       """
#       return
#
#   def test_refine_step(self):
#       """check PdfFit.refine_step()
#       """
#       return
#
#   def test_save_pdf(self):
#       """check PdfFit.save_pdf()
#       """
#       return
#
#   def test_save_pdf_string(self):
#       """check PdfFit.save_pdf_string()
#       """
#       return
#
#   def test_save_dif(self):
#       """check PdfFit.save_dif()
#       """
#       return
#
#   def test_save_dif_string(self):
#       """check PdfFit.save_dif_string()
#       """
#       return
#
#   def test_save_res(self):
#       """check PdfFit.save_res()
#       """
#       return
#
#   def test_save_res_string(self):
#       """check PdfFit.save_res_string()
#       """
#       return

    def test_get_structure(self):
        """check PdfFit.get_structure()
        """
        # skip test when diffpy.Structure is not installed
        try:
            from diffpy.Structure import Structure
        except ImportError:
            return
        self.P.read_struct(testdata('Ni.stru'))
        self.P.read_struct(testdata('PbScW25TiO3.stru'))
        stru1 = self.P.get_structure(1)
        self.assertEqual(4, len(stru1))
        self.assertEqual('Ni', stru1[0].element)
        stru2 = self.P.get_structure(2)
        self.assertEqual(56, len(stru2))
        self.assertEqual('Ti', stru2[-1].element)
        return

#   def test_save_struct(self):
#       """check PdfFit.save_struct()
#       """
#       return
#
#   def test_save_struct_string(self):
#       """check PdfFit.save_struct_string()
#       """
#       return
#
#   def test_show_struct(self):
#       """check PdfFit.show_struct()
#       """
#       return
#
#   def test_constrain(self):
#       """check PdfFit.constrain()
#       """
#       return
#
#   def test_setpar(self):
#       """check PdfFit.setpar()
#       """
#       return
#
#   def test_setvar(self):
#       """check PdfFit.setvar()
#       """
#       return
#
#   def test_getvar(self):
#       """check PdfFit.getvar()
#       """
#       return
#
#   def test_getrw(self):
#       """check PdfFit.getrw()
#       """
#       return
#
#   def test_getR(self):
#       """check PdfFit.getR()
#       """
#       return
#
#   def test_getpdf_fit(self):
#       """check PdfFit.getpdf_fit()
#       """
#       return
#
#   def test_getpdf_obs(self):
#       """check PdfFit.getpdf_obs()
#       """
#       return
#
#   def test_getpdf_diff(self):
#       """check PdfFit.getpdf_diff()
#       """
#       return

    def test_get_atoms(self):
        """check PdfFit.get_atoms()
        """
        self.P.read_struct(testdata('Ni.stru'))
        self.P.read_struct(testdata('PbScW25TiO3.stru'))
        self.P.setphase(1)
        a1 = self.P.get_atoms()
        a2 = self.P.get_atoms(2)
        self.assertEqual(4*['NI'], a1)
        self.assertEqual(8*['PB']+24*['O']+8*['SC']+8*['W']+8*['TI'], a2)
        return

    def test_get_atom_types(self):
        """check PdfFit.get_atom_types()
        """
        self.P.read_struct(testdata('Ni.stru'))
        self.P.read_struct(testdata('PbScW25TiO3.stru'))
        self.P.setphase(1)
        atp1 = self.P.get_atom_types()
        atp2 = self.P.get_atom_types(2)
        self.assertEqual(['NI'], atp1)
        self.assertEqual(['PB', 'O', 'SC', 'W', 'TI'], atp2)
        return

    def test_num_phases(self):
        """check PdfFit.num_phases()
        """
        self.assertEqual(0, self.P.num_phases())
        self.P.read_struct(testdata('Ni.stru'))
        self.assertEqual(1, self.P.num_phases())
        self.P.read_struct(testdata('PbScW25TiO3.stru'))
        self.assertEqual(2, self.P.num_phases())
        self.P.reset()
        self.assertEqual(0, self.P.num_phases())
        return

    def test_num_datasets(self):
        """check PdfFit.num_datasets()
        """
        self.assertEqual(0, self.P.num_datasets())
        self.P.read_data(testdata('Ni.dat'), 'X', 25.0, 0.5)
        self.assertEqual(1, self.P.num_datasets())
        # failed data should not increase num_datasets
        try:
            self.P.read_data(testdata('badNi.dat'))
        except:
            pass
        self.assertEqual(1, self.P.num_datasets())
        # alloc should increase number of datasets
        # alloc requires a loaded structure
        self.P.read_struct(testdata('Ni.stru'))
        self.P.alloc('X', 30.0, 0.05, 2, 10, 100)
        self.assertEqual(2, self.P.num_datasets())
        self.P.reset()
        self.assertEqual(0, self.P.num_datasets())
        return

    def test_getcrw(self):
        """check PdfFit.getcrw()
        """
        import numpy
        self.assertEqual(0, self.P.num_datasets())
        # Setting qmax=0 so that partial crw are not disturbed by
        # termination ripples.
        self.P.read_data(testdata('Ni.dat'), 'X', 0.0, 0.0)
        # crw is empty before data refinement
        self.assertEqual([], self.P.getcrw())
        self.P.read_struct(testdata('Ni.stru'))
        self.P.pdfrange(1, 2, 19)
        self.P.refine()
        crw19 = numpy.array(self.P.getcrw())
        self.failUnless(numpy.all(crw19 >= 0.0))
        # check that crw19 is non decreasing
        self.failUnless(numpy.all(numpy.diff(crw19) >= 0.0))
        # check that crw19 and getrw give the same value
        rw19 = crw19[-1]
        self.assertAlmostEqual(self.P.getrw(), rw19, self.places)
        # renormalize cumulative Rw and compare with Rw at r=15
        Gobs19 = numpy.array(self.P.getpdf_obs())
        Gnorm19 = numpy.sqrt(numpy.sum(Gobs19**2))
        r = numpy.array(self.P.getR())
        idx = numpy.nonzero(r <= 15)[0]
        Gnorm15 = numpy.sqrt(numpy.sum(Gobs19[idx]**2))
        i15 = idx[-1]
        rw15 = crw19[i15] * Gnorm19 / Gnorm15
        self.P.pdfrange(1, 2, r[i15] + 1e-5)
        self.P.refine()
        self.assertAlmostEqual(self.P.getrw(), rw15, self.places)
        return

    def test_getcrw_two_datasets(self):
        """check that getcrw() and getrw() are consistent for two datasets.
        """
        self.P.read_data(testdata('Ni.dat'), 'X', 25.0, 0.0)
        self.P.pdfrange(1, 2, 8)
        self.P.read_data(testdata('300K.gr'), 'N', 32.0, 0.0)
        self.P.pdfrange(2, 1, 11)
        self.P.read_struct(testdata('Ni.stru'))
        # mess lattice parameters to have comparable Rw contributions
        self.P.setvar('lat(1)', 3)
        self.P.setvar('lat(2)', 3)
        self.P.setvar('lat(3)', 3)
        self.P.refine()
        rwtot = self.P.getrw()
        self.failUnless(rwtot > 0.0)
        self.P.setdata(1)
        rw1 = self.P.getcrw()[-1]
        self.P.setdata(2)
        rw2 = self.P.getcrw()[-1]
        self.assertAlmostEqual(rwtot**2, rw1**2 + rw2**2, self.places)
        return

#   def test_getpar(self):
#       """check PdfFit.getpar()
#       """
#       return
#
#   def test_fixpar(self):
#       """check PdfFit.fixpar()
#       """
#       return
#
#   def test_freepar(self):
#       """check PdfFit.freepar()
#       """
#       return
#
#   def test_setphase(self):
#       """check PdfFit.setphase()
#       """
#       return
#
#   def test_setdata(self):
#       """check PdfFit.setdata()
#       """
#       return
#
#   def test_psel(self):
#       """check PdfFit.psel()
#       """
#       return
#
#   def test_pdesel(self):
#       """check PdfFit.pdesel()
#       """
#       return
#
#   def test_selectAtomType(self):
#       """check PdfFit.selectAtomType()
#       """
#       return
#
#   def test_selectAtomIndex(self):
#       """check PdfFit.selectAtomIndex()
#       """
#       return
#
#   def test_selectAll(self):
#       """check PdfFit.selectAll()
#       """
#       return
#
#   def test_selectNone(self):
#       """check PdfFit.selectNone()
#       """
#       return

    def test_bond_angle(self):
        """check PdfFit.bond_angle()
        """
        self.P.read_struct(testdata('Ni.stru'))
        a, e = self.P.bond_angle(1, 2, 3)
        self.assertAlmostEqual(60.0, a, self.places)
        self.assertRaises(ValueError, self.P.bond_angle, 0, 1, 2)
        self.assertRaises(ValueError, self.P.bond_angle, 1, 2, 7)
        return

    def test_bond_length_atoms(self):
        """check PdfFit.bond_length_atoms()
        """
        self.P.read_struct(testdata('Ni.stru'))
        self.P.read_struct(testdata('PbScW25TiO3.stru'))
        dij, ddij = self.P.bond_length_atoms(1, 5)
        self.assertAlmostEqual(4.03635, dij, self.places)
        self.P.setphase(1)
        self.assertRaises(ValueError, self.P.bond_length_atoms, 1, 5)
        return

    def test_bond_length_types(self):
        """check PdfFit.bond_length_types()
        """
        self.P.read_struct(testdata('Ni.stru'))
        self.P.read_struct(testdata('PbScW25TiO3.stru'))
        dPbO = self.P.bond_length_types('Pb', 'O', 0.1, 3.0)
        # check if keys are present
        self.failUnless('dij' in dPbO)
        self.failUnless('ddij' in dPbO)
        self.failUnless('ij0' in dPbO)
        self.failUnless('ij1' in dPbO)
        # check if they have the same length
        npts = len(dPbO['dij'])
        self.assertEqual(npts, len(dPbO['ddij']))
        self.assertEqual(npts, len(dPbO['ij0']))
        self.assertEqual(npts, len(dPbO['ij1']))
        # 8 Pb atoms have coordination 12 in perovskite structure
        self.assertEqual(8*12, len(dPbO['dij']))
        self.P.setphase(1)
        dfcc = self.P.bond_length_types('ALL', 'ALL', 0.1, 2.6)
        # 4 Ni atoms with coordination 12
        self.assertEqual(4*12, len(dfcc['dij']))
        # invalid element
        self.assertRaises(ValueError, self.P.bond_length_types, 'Ni', 'Nix', 0.1, 5.0)
        # check indices ij0
        allij0 = sum(dfcc['ij0'], tuple())
        self.assertEqual(0, min(allij0))
        self.assertEqual(3, max(allij0))
        # check indices ij1
        allij1 = sum(dfcc['ij1'], tuple())
        self.assertEqual(1, min(allij1))
        self.assertEqual(4, max(allij1))
        # check index values
        ij0check = [(i1 - 1, j1 - 1) for i1, j1 in dfcc['ij1']]
        self.assertEqual(ij0check, dfcc['ij0'])
        # test valid element which is not present in the structure
        dnone = self.P.bond_length_types('Ni', 'Au', 0.1, 5.0)
        self.assertEqual(0, len(dnone['dij']))
        self.assertEqual(0, len(dnone['ddij']))
        self.assertEqual(0, len(dnone['ij0']))
        self.assertEqual(0, len(dnone['ij1']))
        return

#   def test_show_scat(self):
#       """check PdfFit.show_scat()
#       """
#       return
#
#   def test_get_scat_string(self):
#       """check PdfFit.get_scat_string()
#       """
#       return

    def test_get_scat(self):
        """check PdfFit.get_scat()
        """
        # x-ray scattering factors
        fPb = self.P.get_scat('X', 'Pb')
        self.assertEqual(82.0, fPb)
        fTi = self.P.get_scat('X', 'tI')
        self.assertEqual(22.0, fTi)
        # neutron scattering lengths
        bPb = self.P.get_scat('N', 'PB')
        self.assertAlmostEqual(9.401, bPb, 3)
        bTi = self.P.get_scat('N', 'ti')
        self.assertAlmostEqual(-3.370, bTi, 3)
        # exceptions
        self.assertRaises(ValueError, self.P.get_scat, 'N', 'zz')
        self.assertRaises(ValueError, self.P.get_scat, 'Z', 'Ti')
        return

    def test_set_scat(self):
        """check PdfFit.set_scat()
        """
        # raises exception when no phase exists
        self.assertRaises(pdffit2.unassignedError,
                self.P.set_scat, 'N', 'Ti', -11)
        # check if it is local to phase
        fPb = self.P.get_scat('X', 'Pb')
        bPb = self.P.get_scat('N', 'Pb')
        self.P.read_struct(testdata('PbScW25TiO3.stru'))
        self.P.set_scat('X', 'Pb', 142)
        self.assertEqual(142, self.P.get_scat('X', 'Pb'))
        self.assertEqual(bPb, self.P.get_scat('N', 'Pb'))
        self.P.read_struct(testdata('PbScW25TiO3.stru'))
        self.assertEqual(fPb, self.P.get_scat('X', 'Pb'))
        self.P.setphase(1)
        self.assertEqual(142, self.P.get_scat('X', 'Pb'))
        self.P.setphase(2)
        self.assertEqual(fPb, self.P.get_scat('X', 'Pb'))
        # check exception for invalid inputs
        self.assertRaises(ValueError, self.P.set_scat, 'Z', 'C', 123)
        self.assertRaises(ValueError, self.P.set_scat, 'X', 'ZZ', 123)
        return

    def test_reset_scat(self):
        """check PdfFit.reset_scat()
        """
        # raises exception when no phase exists
        self.assertRaises(pdffit2.unassignedError, self.P.reset_scat, 'Ti')
        # check if it is local to phase
        fPb = self.P.get_scat('X', 'Pb')
        bPb = self.P.get_scat('N', 'Pb')
        self.P.read_struct(testdata('PbScW25TiO3.stru'))
        self.P.set_scat('X', 'Pb', 142)
        self.P.read_struct(testdata('PbScW25TiO3.stru'))
        self.P.set_scat('N', 'Pb', -17)
        self.P.setphase(1)
        self.assertNotEqual(fPb, self.P.get_scat('X', 'Pb'))
        self.P.reset_scat('Pb')
        self.assertEqual(fPb, self.P.get_scat('X', 'Pb'))
        self.P.setphase(2)
        self.assertNotEqual(bPb, self.P.get_scat('N', 'Pb'))
        self.P.reset_scat('Pb')
        self.assertEqual(bPb, self.P.get_scat('N', 'Pb'))
        # check exception for invalid inputs
        self.assertRaises(ValueError, self.P.reset_scat, 'Zz')
        return

    def test_num_atoms(self):
        """check PdfFit.num_atoms()
        """
        self.P.read_struct(testdata('Ni.stru'))
        self.assertEqual(4, self.P.num_atoms())
        self.P.read_struct(testdata('PbScW25TiO3.stru'))
        self.assertEqual(56, self.P.num_atoms())
        self.P.setphase(1)
        self.assertEqual(4, self.P.num_atoms())
        self.P.setphase(2)
        self.assertEqual(56, self.P.num_atoms())
        return

#   def test_lat(self):
#       """check PdfFit.lat()
#       """
#       return
#
#   def test_x(self):
#       """check PdfFit.x()
#       """
#       return
#
#   def test_y(self):
#       """check PdfFit.y()
#       """
#       return
#
#   def test_z(self):
#       """check PdfFit.z()
#       """
#       return
#
#   def test_u11(self):
#       """check PdfFit.u11()
#       """
#       return
#
#   def test_u22(self):
#       """check PdfFit.u22()
#       """
#       return
#
#   def test_u33(self):
#       """check PdfFit.u33()
#       """
#       return
#
#   def test_u12(self):
#       """check PdfFit.u12()
#       """
#       return
#
#   def test_u13(self):
#       """check PdfFit.u13()
#       """
#       return
#
#   def test_u23(self):
#       """check PdfFit.u23()
#       """
#       return
#
#   def test_occ(self):
#       """check PdfFit.occ()
#       """
#       return
#
#   def test_pscale(self):
#       """check PdfFit.pscale()
#       """
#       return
#
#   def test_pscale(self):
#       """check PdfFit.pscale()
#       """
#       return
#
#   def test_sratio(self):
#       """check PdfFit.sratio()
#       """
#       return
#
#   def test_delta1(self):
#       """check PdfFit.delta1()
#       """
#       return
#
#   def test_delta2(self):
#       """check PdfFit.delta2()
#       """
#       return
#
#   def test_dscale(self):
#       """check PdfFit.dscale()
#       """
#       return
#
#   def test_qdamp(self):
#       """check PdfFit.qdamp()
#       """
#       return
#
#   def test_qbroad(self):
#       """check PdfFit.qbroad()
#       """
#       return
#
#   def test_rcut(self):
#       """check PdfFit.rcut()
#       """
#       return
#
#   def test___init__(self):
#       """check PdfFit.__init__()
#       """
#       return
#
#   def test__PdfFit__getRef(self):
#       """check PdfFit._PdfFit__getRef()
#       """
#       return

# End of class TestPdfFit

if __name__ == '__main__':
    unittest.main()

# End of file
