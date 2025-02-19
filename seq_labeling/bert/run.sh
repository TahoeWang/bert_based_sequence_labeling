export BERT_BASE_DIR=chinese_L-12_H-768_A-12
export DATA_BASE_DIR=../data/
export OUTPUT_DIR=../output

CUDA_VISIBLE_DEVICES=0 python run_classifier.py \
  --task_name=COLA \
  --do_train=true \
  --do_eval=true \
  --do_predict=true \
  --data_dir=$DATA_BASE_DIR \
  --vocab_file=$BERT_BASE_DIR/vocab.txt \
  --bert_config_file=$BERT_BASE_DIR/bert_config.json \
  --init_checkpoint=$BERT_BASE_DIR/bert_model.ckpt \
  --max_seq_length=258 \
  --train_batch_size=16 \
  --learning_rate=1e-5 \
  --num_train_epochs=3.0 \
  --output_dir=$OUTPUT_DIR