cd /home/gaopeng/Desktop/caffe
./build/tools/caffe train \
--solver="models/VGGNet/VOC0712/SSD_300x300/solver.prototxt" \
--weights="models/VGGNet/VGG_ILSVRC_16_layers_fc_reduced.caffemodel" \
--gpu 0 2>&1 | tee jobs/VGGNet/VOC0712/SSD_300x300/VGG_VOC0712_SSD_300x300.log
