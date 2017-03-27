# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Fileinfolist(models.Model):
    ind = models.AutoField(primary_key=True)
    g_file_id = models.CharField(max_length=15, blank=True, null=True)
    data_id = models.SmallIntegerField(blank=True, null=True)
    type_ind = models.IntegerField(blank=True, null=True)
    file_start = models.IntegerField(blank=True, null=True)
    file_end = models.IntegerField(blank=True, null=True)
    archive_file = models.CharField(max_length=255, blank=True, null=True)
    local_file = models.CharField(max_length=255, blank=True, null=True)
    catalog_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'fileinfolist'


class Id1112RsSpectrumPiHe(models.Model):
    index = models.AutoField(primary_key=True)
    rs_id = models.IntegerField(blank=True, null=True)
    start_time = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    sigma = models.FloatField(blank=True, null=True)
    task_id = models.CharField(max_length=40, blank=True, null=True)
    finished_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'id1112-rs-spectrum-pi-he'


class Id1112RsSpectrumPiLe(models.Model):
    index = models.AutoField(primary_key=True)
    rs_id = models.IntegerField(blank=True, null=True)
    start_time = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    sigma = models.FloatField(blank=True, null=True)
    task_id = models.CharField(max_length=40, blank=True, null=True)
    finished_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'id1112-rs-spectrum-pi-le'


class Id1112RsSpectrumPiMe(models.Model):
    index = models.AutoField(primary_key=True)
    rs_id = models.IntegerField(blank=True, null=True)
    start_time = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    sigma = models.FloatField(blank=True, null=True)
    task_id = models.CharField(max_length=40, blank=True, null=True)
    finished_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'id1112-rs-spectrum-pi-me'


class Id1301GpsIntervalHe(models.Model):
    index = models.AutoField(primary_key=True)
    group_id = models.IntegerField(blank=True, null=True)
    start_time = models.IntegerField()
    duration = models.IntegerField(blank=True, null=True)
    min = models.IntegerField(blank=True, null=True)
    max = models.IntegerField(blank=True, null=True)
    data = models.CharField(max_length=80, blank=True, null=True)
    task_id = models.CharField(max_length=40, blank=True, null=True)
    finished_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'id1301_gps_interval_he'


class Id1304GpsIntervalLe(models.Model):
    index = models.AutoField(primary_key=True)
    box_id = models.IntegerField(blank=True, null=True)
    start_time = models.IntegerField()
    duration = models.IntegerField(blank=True, null=True)
    min = models.IntegerField(blank=True, null=True)
    max = models.IntegerField(blank=True, null=True)
    data = models.CharField(max_length=80, blank=True, null=True)
    task_id = models.CharField(max_length=40, blank=True, null=True)
    finished_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'id1304_gps_interval_le'


class Id1307GpsIntervalMe(models.Model):
    index = models.AutoField(primary_key=True)
    fpga_id = models.IntegerField(blank=True, null=True)
    start_time = models.IntegerField()
    duration = models.IntegerField(blank=True, null=True)
    min = models.IntegerField(blank=True, null=True)
    max = models.IntegerField(blank=True, null=True)
    data = models.CharField(max_length=80, blank=True, null=True)
    task_id = models.CharField(max_length=40, blank=True, null=True)
    finished_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'id1307_gps_interval_me'


class Id1311GpsIntervalHeAve(models.Model):
    index = models.AutoField(primary_key=True)
    group_id = models.IntegerField(blank=True, null=True)
    start_time = models.IntegerField()
    duration = models.IntegerField(blank=True, null=True)
    data = models.FloatField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    task_id = models.CharField(max_length=40, blank=True, null=True)
    finished_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'id1311_gps_interval_he_ave'


class Id1314GpsIntervalLeAve(models.Model):
    index = models.AutoField(primary_key=True)
    box_id = models.IntegerField(blank=True, null=True)
    start_time = models.IntegerField()
    duration = models.IntegerField(blank=True, null=True)
    data = models.FloatField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    task_id = models.CharField(max_length=40, blank=True, null=True)
    finished_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'id1314_gps_interval_le_ave'


class Id1317GpsIntervalMeAve(models.Model):
    index = models.AutoField(primary_key=True)
    fpga_id = models.IntegerField(blank=True, null=True)
    start_time = models.IntegerField()
    duration = models.IntegerField(blank=True, null=True)
    data = models.FloatField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    task_id = models.CharField(max_length=40, blank=True, null=True)
    finished_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'id1317_gps_interval_me_ave'


class Id1320RsSpectrumPhaHe(models.Model):
    index = models.AutoField(primary_key=True)
    rs_id = models.IntegerField(blank=True, null=True)
    start_time = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    sigma = models.FloatField(blank=True, null=True)
    task_id = models.CharField(max_length=40, blank=True, null=True)
    finished_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'id1320_rs_spectrum_pha_he'


class Id1323RsSpectrumPhaLe(models.Model):
    index = models.AutoField(primary_key=True)
    rs_id = models.IntegerField(blank=True, null=True)
    start_time = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    sigma = models.FloatField(blank=True, null=True)
    task_id = models.CharField(max_length=40, blank=True, null=True)
    finished_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'id1323_rs_spectrum_pha_le'


class Id1326RsSpectrumPhaMe(models.Model):
    index = models.AutoField(primary_key=True)
    rs_id = models.IntegerField(blank=True, null=True)
    start_time = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    sigma = models.FloatField(blank=True, null=True)
    task_id = models.CharField(max_length=40, blank=True, null=True)
    finished_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'id1326_rs_spectrum_pha_me'


class Id1330CntDiffHe(models.Model):
    index = models.AutoField(primary_key=True)
    det_id = models.IntegerField(blank=True, null=True)
    start_time = models.IntegerField(blank=True, null=True)
    start_time2 = models.DateTimeField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    filename = models.CharField(max_length=80, blank=True, null=True)
    task_id = models.CharField(max_length=40, blank=True, null=True)
    finished_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'id1330_cnt_diff_he'


class Id1333CntDiffHeOoc(models.Model):
    index = models.AutoField(primary_key=True)
    det_id = models.IntegerField(blank=True, null=True)
    start_time = models.IntegerField(blank=True, null=True)
    start_time2 = models.DateTimeField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    filename = models.CharField(max_length=80, blank=True, null=True)
    task_id = models.CharField(max_length=40, blank=True, null=True)
    finished_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'id1333_cnt_diff_he_ooc'


class Id1336CntDiffMe(models.Model):
    index = models.AutoField(primary_key=True)
    fpga_id = models.IntegerField(blank=True, null=True)
    start_time = models.IntegerField(blank=True, null=True)
    start_time2 = models.DateTimeField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    filename = models.CharField(max_length=80, blank=True, null=True)
    task_id = models.CharField(max_length=40, blank=True, null=True)
    finished_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'id1336_cnt_diff_me'


class Id1337CntDiffLe(models.Model):
    index = models.AutoField(primary_key=True)
    fov_id = models.IntegerField(blank=True, null=True)
    start_time = models.IntegerField(blank=True, null=True)
    start_time2 = models.DateTimeField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    filename = models.CharField(max_length=80, blank=True, null=True)
    task_id = models.CharField(max_length=40, blank=True, null=True)
    finished_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'id1337_cnt_diff_le'


class Id1341ForcetriggerIntervalLe(models.Model):
    index = models.AutoField(primary_key=True)
    cds_id = models.IntegerField(blank=True, null=True)
    start_time = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    min = models.IntegerField(blank=True, null=True)
    max = models.IntegerField(blank=True, null=True)
    data = models.CharField(max_length=80, blank=True, null=True)
    task_id = models.CharField(max_length=40, blank=True, null=True)
    finished_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'id1341_forcetrigger_interval_le'


class Id1345NoiseSpectrumLeBox1(models.Model):
    index = models.AutoField(primary_key=True)
    det_id = models.IntegerField(blank=True, null=True)
    start_time = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    pos = models.FloatField(blank=True, null=True)
    sigma = models.FloatField(blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)
    task_id = models.CharField(max_length=40, blank=True, null=True)
    finished_tim = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'id1345_noise_spectrum_le_box1'


class Id1346NoiseSpectrumLeBox2(models.Model):
    index = models.AutoField(primary_key=True)
    det_id = models.IntegerField(blank=True, null=True)
    start_time = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    pos = models.FloatField(blank=True, null=True)
    sigma = models.FloatField(blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)
    task_id = models.CharField(max_length=40, blank=True, null=True)
    finished_tim = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'id1346_noise_spectrum_le_box2'


class Id1347NoiseSpectrumLeBox3(models.Model):
    index = models.AutoField(primary_key=True)
    det_id = models.IntegerField(blank=True, null=True)
    start_time = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    pos = models.FloatField(blank=True, null=True)
    sigma = models.FloatField(blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)
    task_id = models.CharField(max_length=40, blank=True, null=True)
    finished_tim = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'id1347_noise_spectrum_le_box3'


class Id1351EvtCntHe(models.Model):
    index = models.AutoField(primary_key=True)
    start_time = models.IntegerField(blank=True, null=True)
    start_time2 = models.DateTimeField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    filename = models.CharField(max_length=80, blank=True, null=True)
    task_id = models.CharField(max_length=40, blank=True, null=True)
    finished_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'id1351_evt_cnt_he'


class Id1352EvtCntLe(models.Model):
    index = models.AutoField(primary_key=True)
    start_time = models.IntegerField(blank=True, null=True)
    start_time2 = models.DateTimeField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    filename = models.CharField(max_length=80, blank=True, null=True)
    task_id = models.CharField(max_length=40, blank=True, null=True)
    finished_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'id1352_evt_cnt_le'


class Id1353EvtCntMe(models.Model):
    index = models.AutoField(primary_key=True)
    start_time = models.IntegerField(blank=True, null=True)
    start_time2 = models.DateTimeField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    filename = models.CharField(max_length=80, blank=True, null=True)
    task_id = models.CharField(max_length=40, blank=True, null=True)
    finished_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'id1353_evt_cnt_me'


class Id1361OocCntHe(models.Model):
    index = models.AutoField(primary_key=True)
    start_time = models.IntegerField(blank=True, null=True)
    start_time2 = models.DateTimeField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    filename = models.CharField(max_length=80, blank=True, null=True)
    task_id = models.CharField(max_length=40, blank=True, null=True)
    finished_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'id1361_ooc_cnt_he'


class Id1362OocCntLe(models.Model):
    index = models.AutoField(primary_key=True)
    start_time = models.IntegerField(blank=True, null=True)
    start_time2 = models.DateTimeField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    filename = models.CharField(max_length=80, blank=True, null=True)
    task_id = models.CharField(max_length=40, blank=True, null=True)
    finished_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'id1362_ooc_cnt_le'


class Id1363OocCntMe(models.Model):
    index = models.AutoField(primary_key=True)
    start_time = models.IntegerField(blank=True, null=True)
    start_time2 = models.DateTimeField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    filename = models.CharField(max_length=80, blank=True, null=True)
    task_id = models.CharField(max_length=40, blank=True, null=True)
    finished_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'id1363_ooc_cnt_me'


class Id1371AcHe(models.Model):
    index = models.AutoField(primary_key=True)
    det_id = models.IntegerField(blank=True, null=True)
    start_time = models.IntegerField(blank=True, null=True)
    start_time2 = models.DateTimeField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    data = models.CharField(max_length=80, blank=True, null=True)
    task_id = models.CharField(max_length=40, blank=True, null=True)
    finished_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'id1371_ac_he'


class Id1381PhaHeP(models.Model):
    index = models.AutoField(primary_key=True)
    start_time = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    filename = models.CharField(max_length=80, blank=True, null=True)
    task_id = models.CharField(max_length=40, blank=True, null=True)
    finished_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'id1381_pha_he_p'


class Id1383PhaMeP(models.Model):
    index = models.AutoField(primary_key=True)
    unit_type = models.CharField(max_length=4, blank=True, null=True)
    start_time = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    filename = models.CharField(max_length=80, blank=True, null=True)
    task_id = models.CharField(max_length=40, blank=True, null=True)
    finished_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'id1383_pha_me_p'


class Id1389PhaLeP(models.Model):
    index = models.AutoField(primary_key=True)
    unit_type = models.CharField(max_length=4, blank=True, null=True)
    start_time = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    filename = models.CharField(max_length=80, blank=True, null=True)
    task_id = models.CharField(max_length=40, blank=True, null=True)
    finished_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'id1389_pha_le_p'


class Id1401PiHeP(models.Model):
    index = models.AutoField(primary_key=True)
    start_time = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    filename = models.CharField(max_length=80, blank=True, null=True)
    task_id = models.CharField(max_length=40, blank=True, null=True)
    finished_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'id1401_pi_he_p'


class Id1403PiMeP(models.Model):
    index = models.AutoField(primary_key=True)
    unit_type = models.CharField(max_length=4, blank=True, null=True)
    start_time = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    filename = models.CharField(max_length=80, blank=True, null=True)
    task_id = models.CharField(max_length=40, blank=True, null=True)
    finished_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'id1403_pi_me_p'


class Id1409PiLeP(models.Model):
    index = models.AutoField(primary_key=True)
    unit_type = models.CharField(max_length=4, blank=True, null=True)
    start_time = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    filename = models.CharField(max_length=80, blank=True, null=True)
    task_id = models.CharField(max_length=40, blank=True, null=True)
    finished_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'id1409_pi_le_p'


class Id1441PhaHeS(models.Model):
    index = models.AutoField(primary_key=True)
    start_time = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    filename = models.CharField(max_length=80, blank=True, null=True)
    task_id = models.CharField(max_length=40, blank=True, null=True)
    finished_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'id1441_pha_he_s'


class Id1442PhaMeS(models.Model):
    index = models.AutoField(primary_key=True)
    unit_type = models.CharField(max_length=4, blank=True, null=True)
    start_time = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    filename = models.CharField(max_length=80, blank=True, null=True)
    task_id = models.CharField(max_length=40, blank=True, null=True)
    finished_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'id1442_pha_me_s'


class Id1445PhaLeS(models.Model):
    index = models.AutoField(primary_key=True)
    unit_type = models.CharField(max_length=4, blank=True, null=True)
    start_time = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    filename = models.CharField(max_length=80, blank=True, null=True)
    task_id = models.CharField(max_length=40, blank=True, null=True)
    finished_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'id1445_pha_le_s'


class Id1451PiHeS(models.Model):
    index = models.AutoField(primary_key=True)
    start_time = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    filename = models.CharField(max_length=80, blank=True, null=True)
    task_id = models.CharField(max_length=40, blank=True, null=True)
    finished_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'id1451_pi_he_s'


class Id1452PiMeS(models.Model):
    index = models.AutoField(primary_key=True)
    unit_type = models.CharField(max_length=4, blank=True, null=True)
    start_time = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    filename = models.CharField(max_length=80, blank=True, null=True)
    task_id = models.CharField(max_length=40, blank=True, null=True)
    finished_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'id1452_pi_me_s'


class Id1455PiLeS(models.Model):
    index = models.AutoField(primary_key=True)
    unit_type = models.CharField(max_length=4, blank=True, null=True)
    start_time = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    filename = models.CharField(max_length=80, blank=True, null=True)
    task_id = models.CharField(max_length=40, blank=True, null=True)
    finished_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'id1455_pi_le_s'


class Id1461PiMeanHeS(models.Model):
    index = models.AutoField(primary_key=True)
    det_id = models.IntegerField(blank=True, null=True)
    start_time = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    pi_mean = models.FloatField(blank=True, null=True)
    task_id = models.CharField(max_length=40, blank=True, null=True)
    finished_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'id1461_pi_mean_he_s'


class Id1462PiMeanMeS(models.Model):
    index = models.AutoField(primary_key=True)
    unit_type = models.CharField(max_length=4, blank=True, null=True)
    unit_id = models.IntegerField(blank=True, null=True)
    start_time = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    pi_mean = models.FloatField(blank=True, null=True)
    task_id = models.CharField(max_length=40, blank=True, null=True)
    finished_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'id1462_pi_mean_me_s'


class Id1465PiMeanLeS(models.Model):
    index = models.AutoField(primary_key=True)
    unit_type = models.CharField(max_length=4, blank=True, null=True)
    unit_id = models.IntegerField(blank=True, null=True)
    start_time = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    pi_mean = models.FloatField(blank=True, null=True)
    task_id = models.CharField(max_length=40, blank=True, null=True)
    finished_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'id1465_pi_mean_le_s'


class Id1471PulseWidthHe(models.Model):
    index = models.IntegerField(primary_key=True)
    det_id = models.IntegerField(blank=True, null=True)
    start_time = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    pos_na = models.FloatField(blank=True, null=True)
    sigma_na = models.FloatField(blank=True, null=True)
    height_na = models.FloatField(blank=True, null=True)
    pos_cs = models.FloatField(blank=True, null=True)
    sigma_cs = models.FloatField(blank=True, null=True)
    height_cs = models.FloatField(blank=True, null=True)
    ratio = models.FloatField(blank=True, null=True)
    task_id = models.CharField(max_length=40, blank=True, null=True)
    finished_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'id1471_pulse_width_he'


class Id1481EvtIntervalHe(models.Model):
    index = models.AutoField(primary_key=True)
    start_time = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    eff_time = models.IntegerField(blank=True, null=True)
    filename = models.CharField(max_length=80, blank=True, null=True)
    task_id = models.CharField(max_length=40, blank=True, null=True)
    finished_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'id1481_evt_interval_he'


class Id1485EvtIntervalMe(models.Model):
    index = models.AutoField(primary_key=True)
    start_time = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    eff_time = models.IntegerField(blank=True, null=True)
    filename = models.CharField(max_length=80, blank=True, null=True)
    task_id = models.CharField(max_length=40, blank=True, null=True)
    finished_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'id1485_evt_interval_me'


class Id1487EvtIntervalLe(models.Model):
    index = models.AutoField(primary_key=True)
    start_time = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    eff_time = models.IntegerField(blank=True, null=True)
    filename = models.CharField(max_length=80, blank=True, null=True)
    task_id = models.CharField(max_length=40, blank=True, null=True)
    finished_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'id1487_evt_interval_le'


class Id1491PiMeanHeP(models.Model):
    index = models.AutoField(primary_key=True)
    det_id = models.IntegerField(blank=True, null=True)
    start_time = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    pi_mean = models.FloatField(blank=True, null=True)
    task_id = models.CharField(max_length=40, blank=True, null=True)
    finished_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'id1491_pi_mean_he_p'


class Id1495PiMeanMeP(models.Model):
    index = models.AutoField(primary_key=True)
    unit_type = models.CharField(max_length=4, blank=True, null=True)
    unit_id = models.IntegerField(blank=True, null=True)
    start_time = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    pi_mean = models.FloatField(blank=True, null=True)
    task_id = models.CharField(max_length=40, blank=True, null=True)
    finished_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'id1495_pi_mean_me_p'


class Id1501PiMeanLeP(models.Model):
    index = models.AutoField(primary_key=True)
    unit_type = models.CharField(max_length=4, blank=True, null=True)
    unit_id = models.IntegerField(blank=True, null=True)
    start_time = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    pi_mean = models.FloatField(blank=True, null=True)
    task_id = models.CharField(max_length=40, blank=True, null=True)
    finished_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'id1501_pi_mean_le_p'
