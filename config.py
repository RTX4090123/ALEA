import os.path as osp
import argparse
import platform

class config():
    def __init__(self):
        self.this_dir = osp.dirname(__file__)
        self.data_root = osp.abspath(osp.join(self.this_dir, '..', 'data', ''))

    def get_args(self):
        parser = argparse.ArgumentParser()
        """
        primary parameters setting
        """
        parser.add_argument('--gpu', default=0, type=int)
        parser.add_argument('--eval_epoch', default=2, type=int, help='evaluate each n epoch')
        parser.add_argument("--only_test", default=0, type=int, choices=[0, 1])
        parser.add_argument("--data_split", default='norm', type=str, help="Experiment split")
        parser.add_argument("--data_rate", type=float, default=0.2, help="training set rate")
        parser.add_argument('--epoch', default=100, type=int)
        parser.add_argument('--epoch_per_CYCLES', default=50, type=int)
        parser.add_argument('--lr', type=float, default= 1e-3)
        parser.add_argument('--mask', type=float, default=0.1, help='mask probability')
        parser.add_argument("--scheduler", default="cos", type=str, choices=["linear", "cos", "fixed"])
        parser.add_argument("--optim", default="adam", type=str, choices=["adamw", "adam"])
        parser.add_argument("--rho", default=0.1, type=float, help='Lagrange penalty term')
        parser.add_argument("--lambda_", default=0.15, type=float, help='Sparsification strength')
        parser.add_argument("--tau3", default=0.15, type=float, help='truncation value for most valuable potential pair')
        parser.add_argument("--early_stop_threshold", default=1e-7, type=float, help='alternate directions for early stopping')
        parser.add_argument('--CYCLES', default=2, type=int, help='Number of active learning strategy activations. i.e. If CYCLES = 1, it means that the active learning strategy is activated 1 time')
        parser.add_argument("--hidden_units", type=str, default="300,300,300",
                            help="hidden units in each hidden layer(including in_dim and out_dim)")
        parser.add_argument("--save_model", default=0, type=int, choices=[0, 1])
        parser.add_argument('--batch_size', default=3500, type=int)
        parser.add_argument('--semi_learn_step', default=1, type=int, help="semi")
        parser.add_argument("--csls", action="store_true", default=False, help="use CSLS for inference")
        parser.add_argument("--csls_k", type=int, default=3, help="top k for csls")
        parser.add_argument("--data_choice", default="FBDB15K", type=str, choices=["FBYG15K", "FBDB15K"], help="Experiment path")
        parser.add_argument("--random_seed", default=42, type=int)
        parser.add_argument("--exp_id", default="seed_42", type=str, help="Experiment ID")
        parser.add_argument('--workers', type=int, default=12)
        parser.add_argument('--dist', type=int, default=0, help='whether to dist')
        parser.add_argument('--accumulation_steps', type=int, default=1)
        parser.add_argument("--attr_dim", type=int, default=300, help="the hidden size of attr and rel features")
        parser.add_argument("--img_dim", type=int, default=300, help="the hidden size of img feature")
        parser.add_argument("--name_dim", type=int, default=300, help="the hidden size of name feature")
        parser.add_argument("--char_dim", type=int, default=300, help="the hidden size of char feature")
        parser.add_argument("--hidden_size", type=int, default=300, help="the hidden size of MEAformer")
        parser.add_argument("--tau", type=float, default=0.1, help="the temperature factor of contrastive loss")
        parser.add_argument("--tau2", type=float, default=4.0, help="the temperature factor of alignment loss")
        parser.add_argument("--structure_encoder", type=str, default="gat", help="the encoder of structure view", choices=["gat", "gcn"])
        parser.add_argument("--num_attention_heads", type=int, default=1, help="the number of attention_heads of MEAformer")
        parser.add_argument("--num_hidden_layers", type=int, default=1, help="the number of hidden_layers of MEAformer")
        parser.add_argument("--use_surface", type=int, default=0, help="whether to use the surface")
        parser.add_argument("--ratio", type=str, default="1.0", help="which visual adapt",
                            choices=["0.05", "0.1", "0.15", "0.2", "0.3", "0.4",
                                     "0.45", "0.5", "0.55", "0.6", "0.7", "0.75", "0.8", "0.9", "1.0"])
        parser.add_argument("--num_layers", type=int, default=3, help='VAE layers')
        parser.add_argument("--num_layer", type=int, default=3)

        """
        secondary parameters setting
        """
        parser.add_argument("--neg_cross_kg", type=int, default=0,
                            help="whether to force the negative samples in the opposite KG")
        parser.add_argument("--replay", type=int, default=0, help="whether to use replay strategy")
        parser.add_argument("--use_intermediate", type=int, default=1, help="whether to use_intermediate")
        parser.add_argument("--position_embedding_type", default="absolute", type=str)
        parser.add_argument("--intermediate_size", type=int, default=400, help="the hidden size of MEAformer")
        parser.add_argument("--projection", action="store_true", default=False, help="add projection for model")
        parser.add_argument("--alpha", type=float, default=0.2, help="the margin of InfoMaxNCE loss")
        parser.add_argument("--unsup_mode", type=str, default="img", help="unsup mode", choices=["img", "name", "char"])
        parser.add_argument("--unsup_k", type=int, default=1000, help="|visual seed|")
        parser.add_argument("--il_start", type=int, default=500, help="If Il, when to start?")
        parser.add_argument('--margin', default=1, type=float, help='The fixed margin in loss function. ')
        parser.add_argument('--emb_dim', default=1000, type=int, help='The embedding dimension in KGE model.')
        parser.add_argument('--adv_temp', default=1.0, type=float,
                            help='The temperature of sampling in self-adversarial negative sampling.')
        parser.add_argument("--contrastive_loss", default=0, type=int, choices=[0, 1])
        parser.add_argument("--model_name_save", default="", type=str, help="model name for model load")
        parser.add_argument("--model_name", default="MCLEA", type=str, choices=["EVA", "MCLEA", "MSNEA", "MEAformer"], help="model name")
        parser.add_argument("--inner_view_num", type=int, default=6, help="the number of inner view")
        parser.add_argument("--enable_sota", action="store_true", default=False)

        parser.add_argument("--no_tensorboard", default=False, action="store_true")
        parser.add_argument("--exp_name", default="EA_exp", type=str, help="Experiment name")
        parser.add_argument("--dump_path", default="dump/", type=str, help="Experiment dump path")
        parser.add_argument("--data_path", default="mmkg", type=str, help="Experiment path")
        parser.add_argument("--unsup", action="store_true", default=False)
        parser.add_argument("--word_embedding", type=str, default="glove", help="the type of word embedding, [glove|fasttext]", choices=["glove", "bert"])
        parser.add_argument("--es", action="store_true", default=False, help="process the datasets for entity synthesis")
        parser.add_argument('--clip', type=float, default=1., help='gradient clipping')

        parser.add_argument("--with_weight", type=int, default=1, help="Whether to weight the fusion of different ")
        parser.add_argument("--use_project_head", action="store_true", default=False, help="use projection head")

        parser.add_argument("--w_gcn", action="store_false", default=True, help="with gcn features")
        parser.add_argument("--w_rel", action="store_false", default=True, help="with rel features")
        parser.add_argument("--w_attr", action="store_false", default=True, help="with attr features")
        parser.add_argument("--w_name", action="store_false", default=True, help="with name features")
        parser.add_argument("--w_char", action="store_false", default=True, help="with char features")
        parser.add_argument("--w_img", action="store_false", default=True, help="with img features")

        parser.add_argument("--ab_weight", type=float, default=0.5, help="the weight of NTXent Loss")
        parser.add_argument("--zoom", type=float, default=0.1, help="narrow the range of losses")
        parser.add_argument("--reduction", type=str, default="mean", help="[sum|mean]", choices=["sum", "mean"])


        parser.add_argument('--rank', type=int, default=0, help='rank to dist')
        parser.add_argument("--dropout", type=float, default=0.0, help="dropout rate for layers")
        parser.add_argument("--heads", type=str, default="2,2", help="heads in each gat layer, splitted with comma")
        parser.add_argument("--attn_dropout", type=float, default=0.0, help="dropout rate for gat layers")
        parser.add_argument("--instance_normalization", action="store_true", default=False, help="enable instance normalization")
        parser.add_argument("--distance", type=int, default=2, help="L1 distance or L2 distance. ('1', '2')", choices=[1, 2])


        parser.add_argument('--device', default='cuda', help='device id (i.e. 0 or 0,1 or cpu)')
        parser.add_argument('--world-size', default=3, type=int,
                            help='number of distributed processes')
        parser.add_argument('--dist-url', default='env://', help='url used to set up distributed training')
        parser.add_argument("--local_rank", default=-1, type=int)
        parser.add_argument("--il", action="store_true", default=False, help="Iterative learning?")
        parser.add_argument('--weight_decay', type=float, default=0.0001)
        parser.add_argument("--adam_epsilon", default=1e-8, type=float)
        parser.add_argument("--dim", type=int, default=100, help="the hidden size of MSNEA")
        parser.add_argument("--neg_triple_num", type=int, default=1, help="neg triple num")
        parser.add_argument("--use_bert", type=int, default=0)
        parser.add_argument("--use_attr_value", type=int, default=0)

        self.cfg = parser.parse_args()

    def update_configs(self):
        self.cfg.data_root = self.data_root
        self.cfg.data_path = osp.join(self.data_root, self.cfg.data_path)

        if self.cfg.data_choice in ["FBYG15K", "FBDB15K"]:
            self.cfg.use_intermediate = 0
            self.cfg.data_split = "norm"
            self.cfg.inner_view_num = 4
            self.cfg.w_name = False
            self.cfg.w_char = False
            self.cfg.use_surface = 0
            data_split_name = f"{self.cfg.data_rate}_"

        self.cfg.exp_id = f"{'my-solution'}_{self.cfg.data_choice}_{data_split_name}{self.cfg.exp_id}"
        self.cfg.dump_path = osp.join(self.cfg.data_path, self.cfg.dump_path)
        if self.cfg.only_test == 1:
            self.save_model = 0
            self.dist = 0

        self.cfg.dim = self.cfg.attr_dim
        self.cfg.max_position_embeddings = self.cfg.inner_view_num + 1
        assert self.cfg.hidden_size == self.cfg.attr_dim

        return self.cfg



