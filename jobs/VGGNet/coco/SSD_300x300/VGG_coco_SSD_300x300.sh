cd /home/gaopeng/Desktop/caffe
./build/tools/caffe train \
--solver="models/VGGNet/coco/SSD_300x300/solver.prototxt" \
--snapshot="models/VGGNet/coco/SSD_300x300/VGG_coco_SSD_300x300_iter_5.solverstate" \
--gpu 0 2>&1 | tee jobs/VGGNet/coco/SSD_300x300/VGG_coco_SSD_300x300.log
